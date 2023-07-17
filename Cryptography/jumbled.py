import os
from Crypto.Cipher import AES
from secret import flag

secret = b"This is top secret message. I hope, no one can intercept UwU !!!"

iv1 = os.urandom(16)
iv2 = os.urandom(16)
key = os.urandom(16)
flag = flag + b"\0" * (16 - len(flag) % 16)

cipher = AES.new(iv1, AES.MODE_CBC,key)
ciphertext1 = cipher.encrypt(secret)
cipher = AES.new(key, AES.MODE_CBC,iv2)
ciphertext2 = cipher.encrypt(flag)

with open("encrypted", "wb") as f:
    f.write(iv1)
    f.write(ciphertext1)
    f.write(iv2)
    f.write(ciphertext2)
