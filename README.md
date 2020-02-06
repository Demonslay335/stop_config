# stop_config
Dump configuration from STOP Djvu ransomware sample

## Usage
First, unpack malware sample using `dump.py`

```
>python dump.py sample.bin`

...

------------------------------ VirtualProtect (0x27565e) ------------------------------
      _In_  LPVOID lpAddress: 0x400000
      _In_  SIZE_T dwSize: 458752
      _In_  DWORD  flNewProtect: PAGE_EXECUTE_READWRITE
      _Out_ PDWORD lpflOldProtect: 0x18e45c

Param 0: 2578014
Param 1: 4194304
Param 2: 458752
Param 3: 64
Param 4: 1631324
Success dump memory 0x3a0000L to file:dump-2686976.mem
Stopped
```

Then, simply feed dumped sample to `stop_config.py`. Option `-s` can be used to save config to file.

```
>python stop_config.py dump-2686976.mem

File: dump-2686976.mem
[+] Nameserver: ns1.kriston.ug
[+] Nameserver: ns2.chalekin.ug
[+] Nameserver: ns3.unalelath.ug
[+] Nameserver: ns4.andromath.ug
[+] PDB: E:\Doc\My work (C++)\_Git\Encryption\Release\encrypt_win_api.pdb
[+] C2 Path: http://dell1.ug/sdfnbsdfjshfsd57/gdfgdfgdfgdfgdf/get.php
[+] Download: http://dell1.ug/files/penelop/updatewin1.exe
[+] Download: http://dell1.ug/files/penelop/updatewin2.exe
[+] Download: http://dell1.ug/files/penelop/updatewin.exe
[+] Download: http
[+] Download: ://dell1.ug/files/penelop/3.exe
[+] Download: http://dell1.ug/files/penelop/4.exe
[+] Download: http://dell1.ug/files/penelop/5.exe
[+] Email Address: gorentos@bitmessage.ch
[+] Extension: .brusaf
[+] C2 Path: ell1.ug/sdfnbsdfjshfsd57/gdfgdfgdfgdfgdf/get.php
[+] C2 Path: ell1.ug/sdfnbsdfjshfsd57/gdfgdfgdfgdfgdf/get.php
[+] Offline Key: yJpo4ktMNskjzAG6ethjL0npauKrCuHNB1tfpTt2
[+] Offline ID: q9KuzOzkH3m0RZiU9yD24sgV2jlQpgldjv0uODt1
```
