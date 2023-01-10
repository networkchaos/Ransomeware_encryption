#!/usr/bin/env python3

import os

#find all the list 

files = []

for  file in os.listdir():
	if file == "ransome_encrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)


print(files)
