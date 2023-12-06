import socket 
import json 
import Crypto.Util.number
import math
import importlib
bitvector_demo=importlib.import_module("1905067_bitvector_demo")
AES_helper=importlib.import_module("1905067_AES_helper")
ECDH_helper=importlib.import_module("1905067_ECDH_helper")
from BitVector import *

file_path = '/home/sojib/Academics/4-1/Lab/Security/Security_Code/Offline_1/x.png'

with open(file_path, 'rb') as file:
    binary_data = file.read()
byte_array_data = bytearray(binary_data)

print(byte_array_data)

