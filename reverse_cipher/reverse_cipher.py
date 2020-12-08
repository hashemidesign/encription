# Reverse cipher Algorithm
'''
The reverse cipher encrypts a message by printing it in 
reverse order. To decrypt, you simply reverse the reversed 
message to get the original message. ... 
The encryption and decryption steps are the same.
'''

message = "Three can keep a secret, if two of them are dead."
rc_message = ''

i = len(message) - 1  # index
while i >= 0:
    rc_message = rc_message + message[i]
    i = i - 1

# cipher message:
print(rc_message)
