
# Alfabeto sobre el que se trabaja para este caso de criptografía
ALPHABET = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

'''
Función que se necarga de cifrar una letra usando cifrado cesar.
letter es la letra a cifrar y shift es cuánto se correrá esa letra.
Ej: letter = c, shift = 3 -> newLetter = f 
'''
def caesarCipher(letter, shift):
    indexOfLetter = ALPHABET.index(letter)
    newLetter = ALPHABET[(indexOfLetter + shift)%27]
    return newLetter

'''
Función que se necarga de descifrar una letra usando cifrado cesar.
letter es la letra a cifrar y shift es cuánto se correrá esa letra.
Ej: letter = f, shift = 3 -> newLetter = c 
'''
def caesarDecipher(letter, shift):
    indexOfLetter = ALPHABET.index(letter)
    newLetter = ALPHABET[(indexOfLetter - shift)%27]
    return newLetter


'''
Función que se encarga de generar una llave para el cifrado Vegenere.
Ej: text = holamellamojuan, key=papas -> newKey = papaspapaspapas
'''
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

'''
Función que se encarga de generar una autollave para el cifrado Vegenere.
Ej: text = holamellamojuan, key=papas -> newKey = papasholamellam
'''
def generateAutoKey(initialKey, text):
    key = initialKey + text[0:(len(text)-len(initialKey))]
    return key

'''
Función que se encarga de realizar un cifrado Vegenere en función de una llave 
generada con la función generateKey o generateAutoKey.
'''
def vigenereCipher(text, key):
    cipherText = ""
    for i in range(0,len(text)):
        cipherText = cipherText + caesarCipher(text[i], ALPHABET.index(key[i]))
    return cipherText

'''
Función que se encarga de realizar un descifrado Vegenere en función de una llave 
generada con la función generateKey o generateAutoKey.
'''
def vigenereDecipher(text, key):
    decryptText = ""
    for i in range(0,len(text)):
        decryptText = decryptText + caesarDecipher(text[i], ALPHABET.index(key[i]))
    return decryptText

'''
Función que se encarga de realizar un cifrado con una versión modificada del
cifrado Vegenere, el cual consiste en cifrar primeramente con el cifrado Vegenere
utilizando llave normal, y luego, cifrar el texto ya cifrado, utilizando nuevamente
el cifrado Vegenere, con la llave invertida y cifrada.
'''
def modifiedVigenereCipher(text, key):
    key = generateKey(text = text, key = key)
    cipherText = vigenereCipher(text = text, key = key)
    invertedKey = key[::-1] #Se invierte la llave
    invertedCipheredKey = vigenereCipher(key = generateKey(text = invertedKey, key = key), text = invertedKey) #Se cifra la llave invertida con Vegenere
    autoKey = generateAutoKey(initialKey = invertedCipheredKey, text = cipherText) #Se genera la autollave con la llave invertida y cifrada
    cipherText = vigenereCipher(text = cipherText, key = autoKey)
    return cipherText

def modifiedVigenereDecipher(cipherText, key):
    key = generateKey(text = cipherText, key = key)
    decipherText = vigenereDecipher(text = cipherText, key = key)
    invertedKey = key[::-1]
    invertedCipheredKey = vigenereCipher(key = generateKey(text = invertedKey, key = key), text = invertedKey)#Se cifra la llave invertida con Vegenere
    autoKey = generateAutoKey(initialKey = invertedCipheredKey, text = decipherText)#Se genera la autollave con la llave invertida y cifrada
    decipherText = vigenereDecipher(text = decipherText, key = autoKey)
    return decipherText


text = "holamellamojuan"
key = "javo"

'''
EJEMPLO ALGORITMO MODIFICADO
'''
cipherText = modifiedVigenereCipher(text = text, key = key)
decipherText = modifiedVigenereDecipher(cipherText = cipherText, key = key)
print(cipherText)
print(decipherText)

'''
EJEMPLO VIGENERE SIMPLE
'''
cipherText = vigenereCipher(text = text, key = generateKey(text = text, key = key))
decipherText = vigenereDecipher(text = cipherText, key = generateKey(text = text, key = key))
print(cipherText)
print(decipherText)

'''
EJEMPLO VIGENERE CON AUTOLLAVE
'''
cipherText = vigenereCipher(text = text, key = generateAutoKey(text = text, initialKey = key))
decipherText = vigenereDecipher(text = cipherText, key = generateAutoKey(text = text, initialKey = key))
print(cipherText)
print(decipherText)
