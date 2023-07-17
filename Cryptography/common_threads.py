from Crypto.Util.number import getPrime,long_to_bytes,bytes_to_long as b2l
pt = b2l(b'############REDACTED#############')

e1 = 3
e2 = 65537

p = getPrime(512)
q = getPrime(512) 
n = p * q
print("p = ",p)
print("q = ",q)
print("n = ",n)

ct1 = pow(pt,e1,n)
ct2 = pow(pt,e2,n)

print("ct_1 = ",ct1)
print("ct_2 = ",ct2)