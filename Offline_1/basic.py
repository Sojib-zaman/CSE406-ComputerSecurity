import socket 
import ECDH_helper
import json 
import Crypto.Util.number
import math
import AES_helper
from BitVector import *

IV =  BitVector(textstring="\0")
print(IV)
print(IV.length())
given_plaintext="abraras eset t set s c"
print(given_plaintext)
A=Crypto.Util.number.getRandomNBitInteger(128) 
IV = BitVector(intVal=A, size=128)
chunk_count = math.ceil(len(given_plaintext) / 16)


for chunk in range(0,chunk_count,1):
    plaintext=given_plaintext[16*chunk:16*(chunk+1)]
    print(plaintext)
    print(BitVector(textstring=plaintext))
    print(IV)
    plaintext = BitVector(textstring=plaintext)^IV 
    print(plaintext)
