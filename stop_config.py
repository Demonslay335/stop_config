import os, sys, string, re, os, argparse, pefile
from itertools import chain

# https://stackoverflow.com/a/17197027/1301139
def strings(buffer, min=4, max=10000):
	result = ""
	for c in buffer:
		if chr(c) in string.printable:
			result += chr(c)
			continue
		if len(result) >= min and len(result) <= max:
			yield result
		result = ""
	if len(result) >= min and len(result) <= max:  # catch result at EOF
		yield result

# Double-check it is an executable
def isexe(path):
	with open(path, 'rb') as f:
		return f.read()[:2] == 'MZ'

# Check if file appears to be packed
def ispacked(path):
	try:
		# Iterate strings
		pe = pefile.PE(args.path, fast_load=True)
		pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']])
		for entry in pe.DIRECTORY_ENTRY_IMPORT:
			if entry.dll == 'ADVAPI32.dll':
				for imp in entry.imports:
					if imp.name == 'CryptCreateHash':
						return False
	except:
		return True
	return True

def process_file(path, args, key=0x80):
	# Verify it is a file and executable
	if not os.path.isfile(path) or not isexe(path):
		return
	
	# Check for packing
	if ispacked(path):
		print "[-] File appears to be packed"
		return
	
	file = bytearray(open(path, 'rb').read())
	xored = bytearray(len(file))

	for i in xrange(len(file)):
		xored[i] = file[i] ^ key

	rsa = ''
	
	output = 'File: %s' % path
	
	pid_flag = False
	
	for str in chain(strings(file), strings(xored)):
		for s in str.splitlines():
			if re.match(r"^[http://]?.*\.[a-z]{2,}\/", s):
				if '/get.php' in s or '/get_v2.php' in s:
					output += '\n[+] C2 Path: %s' % s
				else:
					if '$run ' in s:
						for d in s.split('$run '):
							output += '\n[+] Download: %s' % d.lstrip('n').rstrip('$ru').rstrip('$run').strip()
					elif 'we.tl' not in s and 'OpenSSL' not in s:
						output += '\n[+] Download: %s' % s
			elif re.match(r"ns[0-9]?\.[a-z0-9]+\.[a-z]+", s):
				output += '\n[+] Nameserver: %s' % s
			elif '.pdb' in s:
				output += '\n[+] PDB: %s' % s
			elif re.match(r"[0-9a-zA-Z]{38}t2", s):
				output += '\n[+] Offline Key: %s' %s
			elif re.match(r"[0-9a-zA-Z]{38}t1", s) or re.match(r"^[0-9a-zA-Z]{40}$", s):
				output += '\n[+] Offline ID: %s' % s
			elif 'BgIAAA' in s or re.match(r"^[a-zA-Z0-9\+\/]{150}$", s) or re.match(r"^[a-zA-Z0-9\+\/]{68}$", s):
				rsa = rsa + s
			elif 'BEGIN PUBLIC KEY' in s or 'END PUBLIC KEY' in s or re.match(r"^[a-zA-Z0-9\+\/\\\-]{150}$", s):
				rsa = rsa + s
			elif re.match(r"[a-z]+@[a-z]+\.[a-z]+", s):
				output += '\n[+] Email Address: %s' % s
			elif re.match(r"^@[a-z]{4,}$", s):
				output += '\n[+] Telegram: %s' % s
			elif re.match(r"\.[a-z]{3,7}$", s) and '.text' not in s and '.rsrc' not in s:
				output += '\n[+] Extension: %s' % s
			elif 'personal ID' in s:
				pid_flag = True
			elif pid_flag and re.match(r'^\d{3,4}([a-zA-Z0-9]{4,})?$', s):
				output += '\n[+] Version String: %s' %s
				pid_flag = False
#			else:
#				print '[%d] %s' % (len(s), s)

	if len(rsa):
		output += '\n[+] Offline RSA Public Key: %s' % rsa.replace('\\n', '').replace('\\', '')
	
	output += '\n'
	
	if args.save:
		with open('stop_config.txt', 'ab') as f:
			f.write(output)
		print '[!] Written to: stop_config.txt'
	
	print output

# Setup argument parser
parser = argparse.ArgumentParser(description='Extract configuration from STOP Djvu ransomware')
parser.add_argument('path', help='executable path or folder')
parser.add_argument('-s, --save', dest='save', help='save config', action='store_true')

# Parse arguments
args = parser.parse_args()

# Check for path
if os.path.isdir(args.path):
	# Iterate files
	for root, dirs, files in os.walk(args.path):
		for filename in files:
			# Process the file
			process_file(os.path.join(root, filename), args)
	
# Check for file
elif os.path.isfile(args.path):
	# Process the file
	process_file(args.path, args)
else:
	print "[-] Invalid executable"