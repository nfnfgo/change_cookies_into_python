import time
import os

print(os.getcwd())

with open('./text.txt','r') as f:
    text=f.read()

print(text)