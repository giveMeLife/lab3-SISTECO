import hashlib
import Crypto

ALPHABET = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def caesarCipher(letter, shift):
    indexOfLetter = ALPHABET.index(letter)
    newLetter = ALPHABET[(indexOfLetter + shift)%27]
    return newLetter

def caesarDecipher(letter, shift):
    indexOfLetter = ALPHABET.index(letter)
    newLetter = ALPHABET[(indexOfLetter - shift)%27]
    return newLetter

def generateAutoKey(initialKey, text):
    key = initialKey + text[0:(len(text)-len(initialKey))]
    return key

def vigenereCipher(text, key):
    cipherText = ""
    for i in range(0,len(text)):
        cipherText = cipherText + caesarCipher(text[i], ALPHABET.index(key[i]))
    return cipherText

def vigenereDecipher(text, key):
    decryptText = ""
    for i in range(0,len(text)):
        decryptText = decryptText + caesarDecipher(text[i], ALPHABET.index(key[i]))
    return decryptText


def generateKey(text, key):
    newKey = ""
    j = 0
    key_length = len(key)
    for i in range(0, len(text)):
        newKey = newKey + key[j]
        j = j+1
        if j == key_length:
            j = 0
    return newKey

text = "holamellamojuan"
key = "skoper"
key = generateKey(text=text, key=key)
cipherText = vigenereCipher(text = text, key = key)
print(cipherText)
key2 = generateAutoKey(text=cipherText, initialKey=key)
cipherText = vigenereCipher(text = cipherText, key = key2)
print(cipherText)

key = "sokper"
key = generateKey(text = cipherText, key = key)
decipherText = vigenereDecipher(text = cipherText, key = key)
print(decipherText)
key2 = generateAutoKey(text=decipherText, initialKey=key)
decipherText = vigenereDecipher(text = decipherText, key = key2)
print(decipherText)

'''print(caesarCipher("c", 25))
key = input("ingrese llave para encriptar: ")
text = "Hola me llamo Juan"
text = text.lower()
text = text.replace(" ","")
key = generateAutoKey(initialKey = key, text = text)
cipherText = vigenereCipher(text = text, key = key)

key = input("ingrese llave para desencriptar: ")
key = generateAutoKey(initialKey = key, text = text)
decryptText = vigenereDecipher(cipherText, key)
print(cipherText)
print(decryptText)'''
'''
byte = "javo".encode()
print(byte)
print(bin(int.from_bytes(byte, "big")))

b = bin(int.from_bytes(byte, "big"))

b = "0"+str(b)[2:len(str(b))]
split_strings = []
for index in range(0, len(b), 8):
    split_strings.append(b[index:index+8])

print(split_strings)
split_strings[len(split_strings)-1] 
print(b)
string = ""
for binary in split_strings:
    an_integer = int(binary, 2)
    char = chr(an_integer)
    string += char

print(string)'''