from gmpy2 import next_prime,invert
from Crypto.Util.number import *

flag = "flag{REDACTED}"
flag = bytes_to_long(flag.encode())
p = getPrime(512)
q = next_prime(p)
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = invert(e,phi)
c = pow(flag,e,n)
print("n : ",n)
print("c : ",c)
