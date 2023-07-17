
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}'
key = ???
flag = ???

def encrypt(plaintext, key):
    
    plaintext = plaintext.upper()
    key = key.upper()
    char_to_val = {char:val for val,char in enumerate(letters)}
    ciphertext = ""

    for i, char in enumerate(plaintext):
        plaintext_val = char_to_val[char]
        key_val = char_to_val[key[i % len(key)]]
        cipher_val = (plaintext_val + key_val) % len(letters)
        cipher_char = letters[cipher_val]
        ciphertext += cipher_char

    return ciphertext

print(encrypt(flag,key))