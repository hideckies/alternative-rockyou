# Alternative RockYou

This repository contains various encoded **rockyou.txt**.  

To use them, you need to extract as follow.

```sh
gunzip base64-rockyou.txt.gz
```

## Generate from Script

If you want to generate some encoded **rockyou.txt** from Python script, run the following command.  
Assume your system locates **rockyou.txt** under **`/usr/share/wordlists/`**.

```sh
# Base32
python3 generator.py base32 > base32-rockyou.txt
# Base64
python3 generator.py base64 > base64-rockyou.txt
```
