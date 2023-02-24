import base64
import codecs
import hashlib
import sys


def main():
    etype = sys.argv[1]

    with codecs.open('/usr/share/wordlists/rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
        words = [w.rstrip() for w in f.readlines()]
    
    for word in words:
        if etype == "base32":
            encoded = base64.b32encode(codecs.encode(word, 'ascii', errors='ignore'))
            print(encoded)
        elif etype == "base64":
            encoded = base64.b64encode(codecs.encode(word, 'ascii', errors='ignore'))
            print(encoded)
        elif etype == "md5":
            encoded = hashlib.md5(codecs.encode(word, 'ascii', errors='ignore'))
            print(encoded.hexdigest())
        elif etype == "sha256":
            encoded = hashlib.sha256(codecs.encode(word, 'ascii', errors='ignore'))
            print(encoded.hexdigest())
        elif etype == "sha512":
            encoded = hashlib.sha512(codecs.encode(word, 'ascii', errors='ignore'))
            print(encoded.hexdigest())


if __name__ == '__main__':
    main()