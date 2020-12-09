# Columnar Transposition Cipher
'''
--> A simple example for a transposition cipher is 
    columnar transposition cipher where each character in the plain text 
    is written horizontally with specified alphabet width. 
    The cipher is written vertically, which creates an entirely 
    different cipher text.

*** EXAMPLE:
 - - - -
|H|e|l|l|
 - - - -
|o|w|o|r|
 - - - -
|l|d| | |
 - - - -
(output) => Holewdlolr


*** Cryptanalysts observed a significant improvement in crypto security 
    when transposition technique is performed. They also noted that 
    re-encrypting the cipher text using same transposition cipher 
    creates better security.
'''


def encryptMessage(key, message):
    # generate columns as an array
    ciphertext = [''] * key
    
    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key

    return ''.join(ciphertext)


myMessage = 'Transposition Cipher'
myKey = 10
ciphertext = encryptMessage(myKey, myMessage)
ciphertext2 = encryptMessage(myKey, ciphertext)
print(ciphertext)
print(ciphertext2)
