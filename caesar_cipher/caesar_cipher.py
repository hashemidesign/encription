# Algorithm of Caesar Cipher

'''
Each letter of plain text is replaced by a letter with some 
fixed number of positions down with alphabet.

--> The chr() method returns a character (a string) 
    from an integer (represents unicode code point 
    of the character).
--> The ord() function returns an integer 
    representing the Unicode character.
--> space(' ') is considered as lowercase, ord(' ') = 32

*** CEASAR ALGORITHM ENCODING:
    -------------------------
    (plain_letter_index + shift_step) % (total_letter_numbers)
    ex: A=0 s=2 ==> (0 + 2) % 26 = 2 : C

*** CEASAR ALGORITHM DECODING:
    -------------------------
    (cipher_letter_index - shift_step + total_letter_numbers) % total_letter_numbers
'''


text = "Two In One Row"
s = 4


def encrypt(text, s):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            # Encrypt uppercase characters in plain text
            # ord('A') = 65, ord('Z')=90
            shifted_char = chr((ord(char) - 65 + s) % 26 + 65)
        else:
            # Encrypt lowercase characters in plain text
            # ord('a') = 97, ord('z') = 122
            shifted_char = chr((ord(char) + s - 97) % 26 + 97)
        result += shifted_char
    return result


def decrypt(cipher, s):
    # (cipher_letter_index - shift_step + total_letter_numbers) % total_letter_numbers
    decoded = ''

    for i in range(len(cipher)):
        char = cipher[i]

        if char.isupper():
            shifted_char = chr((ord(char) - 65 - s + 26) % 26 + 65)
        else:
            shifted_char = chr((ord(char) - 97 - s + 26) % 26 + 97)
        decoded += shifted_char
    return decoded


print(f'tex: {text}, s: {s}')
e = encrypt(text=text, s=s)
print(f'encryption: {e}')
d = decrypt(cipher=e, s=s)
print(f'decryption: {d}')