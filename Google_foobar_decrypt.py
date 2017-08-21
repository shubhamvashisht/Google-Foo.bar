#Encrypting Google foo.bar 2017 encrypted message
#Algo-> Decode the message string to base64 bytes.
#       and do XOR of decoded bytes with your Google username.

import base64

#The encrypted key
message=''

#Your Google username
key='vashisht.s21295'

decrypted_message=[]

#decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

#XOR with Username
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

#The encypted message
print("".join(decrypted_message))
