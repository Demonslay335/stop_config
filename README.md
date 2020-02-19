# stop_config
Dump configuration from STOP Djvu ransomware sample

## Usage
First, unpack malware sample using `dump.py`

```
>python dump.py sample.bin

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

>python stop_config.py dump-60817408.mem

File: dump-60817408.mem
[+] Nameserver: ns1.kriston.ug
[+] Nameserver: ns2.chalekin.ug
[+] Nameserver: ns3.unalelath.ug
[+] Nameserver: ns4.andromath.ug
[+] PDB: E:\Doc\My work (C++)\_Git\Encryption\Release\encrypt_win_api.pdb
[+] C2 Path: http://mohd1.ug/Asjdi435784ihjk65pen2/get.php
[+] Download: http://mohd1.ug/files/penelop/updatewin1.exe
[+] Download: http://mohd1.ug/files/penelop/updatewin2.exe
[+] Download: http://mohd1.ug/files/penelop/updatewin.exe
[+] Download: http
[+] Download: ://mohd1.ug/files/penelop/3.exe
[+] Download: http://mohd1.ug/files/penelop/4.exe
[+] Download: http://mohd1.ug/files/penelop/5.exe
[+] Email Address: helpmanager@mail.ch
[+] Email Address: helpdatarestore@firemail.cc
[+] Email Address: helpmanager@mail.ch
[+] Extension: .ooss
[+] C2 Path: /mohd1.ug/Asjdi435784ihjk65pen2/get.php
[+] C2 Path: /mohd1.ug/Asjdi435784ihjk65pen2/get.php
[+] Offline ID: uvEETK84RPC0Q5icp67CP746LJaCJuwq2tG9Kjt1
[+] Offline RSA Public Key: -----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyqHbz/CXFHoiZIvgiwCuFobWShAU+Bm5z7trSSvje6o6JmGq1CGmXA6MkKDXUxxJpTnWhty28iTUudnc5l7ciW5U7PN++q3pmGOM4RY81f6tmhYJKe6t75W0MDiSP8r7Nzr+2VuLHhmnxQVHaF+G2YgBm7kyDfDNC1iDdZDIYej2tdu38vb/BvUnAdt4XggFAOu5C5BRvIltuwT9BVDRqLy22ZUTJV6eWj+sFCCkIgBvf4yBK3iQRaU0VFDxyyLLsj/JKMD135VxMQe3Tlc4I9hkjMIMX4V06/CH9QT4VtUZp4eGmx17hEBm2V9ES8y5RLQM3b6O3Vd5up478JKxNwIDAQAB-----END PUBLIC KEY-----

```
