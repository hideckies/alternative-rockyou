# Alternative Rockyou

This repository contains various encoded **rockyou.txt** such as **base64-rockyou.txt**, **md5-rockyou.txt**, and so on.  

To use them immediately, download from **[release page](https://github.com/hideckies/alternative-rockyou/releases)** and extract it as follow.

```sh
gunzip base64-rockyou.txt.gz
```

## Generate Rockyou from Script

If you want to generate some encoded **rockyou.txt** from Python script, run the following command.  
Assume your system locates **rockyou.txt** under **`/usr/share/wordlists/`**.

```sh
# Base32
python3 generator.py base32 > base32-rockyou.txt
# Base64
python3 generator.py base64 > base64-rockyou.txt
# MD5
python3 generator.py md5 > md5-rockyou.txt
# SHA256
python3 generator.py sha256 > sha256-rockyou.txt
# SHA512
python3 generator.py sha512 > sha512-rockyou.txt
```
