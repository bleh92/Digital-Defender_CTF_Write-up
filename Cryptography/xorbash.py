import base64

def affine_cipher(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse_alphabet = alphabet[::-1]
    result = ""
    for char in text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            reversed_char = reverse_alphabet[index]
            result += reversed_char
        elif char =='_':
            result +='_'
        else:
            result += char
    return result

def xor_cipher(text,key):
    encrypted_text = affine_cipher(text)
    a = encrypted_text.encode('utf-8')
    b = key.encode('utf-8')
    encrypted_bytes = bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])
    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_text

text = ???
key = 'zoro' 
xor_cipher(text, key)


