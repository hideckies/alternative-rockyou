import base64
import codecs
import sys

def main():
    etype = sys.argv[1]

    with codecs.open('/usr/share/wordlists/rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
        words = [w.rstrip() for w in f.readlines()]
    
    for word in words:
        if etype == "base16":
            encoded = base64.b16encode(codecs.encode(word, 'ascii', errors='ignore'))
        elif etype == "base32":
            encoded = base64.b32encode(codecs.encode(word, 'ascii', errors='ignore'))
        elif etype == "base64":
            encoded = base64.b64encode(codecs.encode(word, 'ascii', errors='ignore'))
        elif etype == "base85":
            encoded = base64.b85encode(codecs.encode(word, 'ascii', errors='ignore'))

        print(encoded.decode('utf-8'))


if __name__ == '__main__':
    main()