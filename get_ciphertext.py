from pyDes import *


def main():
    with open('plaintext.txt', 'r') as file:
        data = file.read()
        k = des("HALLOWEL", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        d = k.encrypt(data)
        # assert k.decrypt(d, padmode=PAD_PKCS5) == data
        print(d)
    #with open('ciphertext.txt', 'wb') as f:
    #   f.write(d) 

chars = sorted({chr(i) for i in range(128)} )
print(bytes(chars[15], encoding='ascii'))