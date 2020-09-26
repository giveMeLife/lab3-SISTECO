import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

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

def graficoEncriptación():
    #Datos
    cantidadBarras=5
    cipherText_modified_throughput = [4/5.99,8/2.99,16/2.99,32/3.99,64/2.99]
    cipherText_simple_throughput = [4/1,8/1,16/0.99,32/1,64/3]
    cipherText_autokey_throughput = [4/0.5,8/0.99,16/1,32/1,64/1.99]
    valoresEje=['4','8','16','32','64']
    indices=np.arange(cantidadBarras)
    anchoBarra=0.25
    rects1 =plt.bar(indices,cipherText_modified_throughput,anchoBarra,color='red',label='Modified Algorithm')
    rects2 =plt.bar(indices+anchoBarra,cipherText_simple_throughput,anchoBarra,color='blueviolet',label='Simple Vigenere')
    rects3 =plt.bar(indices+anchoBarra+anchoBarra,cipherText_autokey_throughput,anchoBarra,color='green',label='AutoKey Vigenere')
    plt.xlabel('Tamaño del Bloque')
    plt.ylabel('Throughput')
    plt.title('Throughput vs Tamaño de Bloque (Encriptación)')
    plt.xticks(indices+anchoBarra,valoresEje)
    plt.legend()
    plt.show()

def graficoDesencriptacion():
    #Datos
    cantidadBarras=5
    cipherText_modified_throughput = [4/3.99,8/2.99,16/2.99,32/2.99,64/3.99]
    cipherText_simple_throughput = [4/0.99,8/0.99,16/2.00,32/0.99,64/1.21]
    cipherText_autokey_throughput = [4/1,8/0.99,16/0.99,32/0.99,64/0.99]
    valoresEje=['4','8','16','32','64']
    indices=np.arange(cantidadBarras)
    anchoBarra=0.25
    rects1 =plt.bar(indices,cipherText_modified_throughput,anchoBarra,color='red',label='Modified Algorithm')
    rects2 =plt.bar(indices+anchoBarra,cipherText_simple_throughput,anchoBarra,color='blueviolet',label='Simple Vigenere')
    rects3 =plt.bar(indices+anchoBarra+anchoBarra,cipherText_autokey_throughput,anchoBarra,color='green',label='AutoKey Vigenere')
    plt.xlabel('Tamaño del Bloque')
    plt.ylabel('Throughput')
    plt.title('Throughput vs Tamaño de Bloque (Desencriptación)')
    plt.xticks(indices+anchoBarra,valoresEje)
    plt.legend()
    plt.show()
    

# Modified
# hmqrnxrñujfg
# dmjñnpññnffy
# 010010010010 4/12

          # Simple               # Modified             # AutoKey
# key          # zejkfpkgnbxy         # hmqrnxrñujfg         # zejpbcadgrvo
# keu         # zefkfmkgjbxu         # dmjñnpññnffy         # zefpbcadgrvo
          # 110110110110 8/12    # 010010010010 4/12    # 110111111111 11/12

# AutoKey
# zejpbcadgrvo
# zefpbcadgrvo
# 110111111111 11/12

# Salidas

text = "palabracorta"
key = "key"

print("Text used:")
print(text)
print(" ")
print("Key used:")
print(key)
print(" ")

'''
EJEMPLO ALGORITMO MODIFICADO
'''

start_cipher = dt.datetime.now()
cipherText = modifiedVigenereCipher(text = text, key = key)
elapsed_cipher =  dt.datetime.now() - start_cipher

start_decipher = dt.datetime.now()
decipherText = modifiedVigenereDecipher(cipherText = cipherText, key = key)
elapsed_decipher =  dt.datetime.now() - start_decipher

print("Cipher Text with Modified Algorithm:",cipherText)
# print("(Modified Algorithm) Time Elapsed Cipher:",elapsed_cipher.total_seconds() * 1000,"with block size:",len(key))
print("Decipher Text with Modified Algorithm:",decipherText)
# print("(Modified Algorithm) Time Elapsed Decipher:",elapsed_decipher.total_seconds() * 1000,"with block size:",len(key))
print(" ")

'''
EJEMPLO VIGENERE SIMPLE
'''

start_cipher = dt.datetime.now()
cipherText = vigenereCipher(text = text, key = generateKey(text = text, key = key))
elapsed_cipher = dt.datetime.now() - start_cipher

start_decipher = dt.datetime.now()
decipherText = vigenereDecipher(text = cipherText, key = generateKey(text = text, key = key))
elapsed_decipher = dt.datetime.now() - start_decipher

print("Cipher Text with Simple Vigenere:",cipherText)
# print("(Simple Vigenere) Time Elapsed Cipher:",elapsed_cipher.total_seconds() * 1000,"with block size:",len(key))
print("Decipher Text with Simple Vigenere:",decipherText)
# print("(Simple Vigenere) Time Elapsed Decipher:",elapsed_decipher.total_seconds() * 1000,"with block size:",len(key))
print(" ")

'''
EJEMPLO VIGENERE CON AUTOLLAVE
'''

start_cipher = dt.datetime.now()
cipherText = vigenereCipher(text = text, key = generateAutoKey(text = text, initialKey = key))
elapsed_cipher = dt.datetime.now() - start_cipher

start_decipher = dt.datetime.now()
decipherText = vigenereDecipher(text = cipherText, key = generateAutoKey(text = text, initialKey = key))
elapsed_decipher = dt.datetime.now() - start_decipher

print("Cipher Text with AutoKey Vigenere:",cipherText)
# print("(AutoKey Vigenere) Time Elapsed Cipher:",elapsed_cipher.total_seconds() * 1000,"with block size:",len(key))
print("Decipher Text with AutoKey Vigenere:",decipherText)
# print("(AutoKey Vigenere) Time Elapsed Decipher:",elapsed_decipher.total_seconds() * 1000,"with block size:",len(key))
print(" ")

# graficoEncriptación()
# graficoDesencriptacion()