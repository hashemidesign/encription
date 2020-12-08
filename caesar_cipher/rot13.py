# ROT13 Algorithm

'''
--> ROT13 cipher refers to the abbreviated form Rotate by 13 
    places. It is a special case of Caesar Cipher in which 
    shift is always 13. 
    Every letter is shifted by 13 places to encrypt or 
    decrypt the message.
--> The ROT13 algorithm uses 13 shifts. Therefore, it is very 
    easy to shift the characters in the reverse manner 
    to decrypt the cipher text.
--> Therefore, it does not include any practical use.

--> The maketrans() method returns a mapping table that can 
    be used with the translate() method to replace specified 
    characters.
    * SYNTAX: string.maketrans(x, y, z)
        - x Required.
        - y is a string with the same length as parameter x.
        - z Optional. 
            A string describing which characters to 
            remove from the original string.
    * EXAMPLE:
        txt = "Good night Sam!";
        x = "mSa";
        y = "eJo";
        z = "odnght";
        mytable = txt.maketrans(x, y, z);
        print(txt.translate(mytable));
'''


rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

# Function to translate plain text
def rot13(text):
   return text.translate(rot13trans)

txt = "ROT13 Algorithm"
print(rot13(txt))
