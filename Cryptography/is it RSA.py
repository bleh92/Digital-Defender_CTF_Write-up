from Crypto.Util.number import getPrime

p = getPrime(1024)
q = getPrime(1024)
r = getPrime(1024)
s = getPrime(1024)

m = #REDACTED
n1 = p*q
n2 = q*r
n3 = #REDACTED
e = 65537
c = pow(m,e,n3)

with open("cipher.txt","w") as f1:
    f1.write("n1 : {n1}\nn2 : {n2}\nn3 : {n3}\nc : {c}")
