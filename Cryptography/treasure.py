import os
from Crypto.Cipher import AES

KEY = 

class CustomCounter(object):
    def __init__(self, value=os.urandom(16), step_up=False):
        self.value = value.hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.new_value = hex(int(self.value, 16) + self.step)
        else:
            self.new_value = hex(int(self.value, 16) - self.stup)
        self.value = self.new_value[2:]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value


def encrypt():
    cipher = AES.new(KEY, AES.MODE_ECB)
    ctr = CustomCounter()
    output = []
    with open("//home//disco//Desktop//flag.png", 'rb') as file:
        block = file.read(16)
        while block:
            keystream = cipher.encrypt(ctr.increment())
            xored = [x^y for x, y in zip(block, keystream)]
            output.append(bytes(xored).hex())
            block = file.read(16)

    return {"encrypted": ''.join(output)}

with open('/home/disco/Desktop/chall.txt','w') as chall:
    chall.write(encrypt()['encrypted'])
