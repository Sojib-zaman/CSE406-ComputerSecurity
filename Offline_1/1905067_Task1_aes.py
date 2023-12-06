from BitVector import * 
import importlib
bitvector_demo=importlib.import_module("1905067_bitvector_demo")
AES_helper=importlib.import_module("1905067_AES_helper")
Helper = importlib.import_module("1905067_Helper")
import time
import math
import Crypto.Util.number
# initial_key="Thats my Kung Fu"
# given_plaintext="Two One Nine Two"

# initial_key = "BUET CSE19 Batch"
# given_plaintext="Never Gonna Give"


# initial_key = "BUET CSE19 Batch"
# given_plaintext="Never Gonna Give you up"

initial_key=input("Input a 128 bit key : ")
initial_key = AES_helper.keychecker(initial_key)
print("Key:")
AES_helper.initial_Print(initial_key)
print()



given_plaintext=input("Input the plaintext to be sent : ")
given_plaintext=AES_helper.plaintextchecker(given_plaintext)


print("Plain Text:")
AES_helper.initial_Print(given_plaintext)
print()


Key_ScheduingStart=time.time()
roundkeys=[]
roundkeys.append(BitVector(textstring=initial_key))
for i in range(0,10,1): 
    roundkeys.append(AES_helper.create_roundkey(roundkeys[i],AES_helper.round_constant_tuple[i]))
Key_ScheduingEnd=time.time()



EncryptionStart=time.time()
final_ciphertext=BitVector(size=0)
A=Crypto.Util.number.getRandomNBitInteger(128) 
IV = BitVector(intVal=A, size=128)
chunk_count = math.ceil(len(given_plaintext) / 16)


for chunk in range(0,chunk_count,1):
    plaintext=given_plaintext[16*chunk:16*(chunk+1)]
    plaintext = BitVector(textstring=plaintext)^IV 
    stateMatrix = AES_helper.createMatrix(roundkeys[0])
    plainMatrix = AES_helper.createMatrix(plaintext)
    stateMatrix = AES_helper.addRoundKey(stateMatrix , plainMatrix)
    for iteration in range (0,10,1):
        stateMatrix=AES_helper.encryption(stateMatrix,AES_helper.createMatrix(roundkeys[iteration+1]),iteration)
    CipherText = AES_helper.createBitVector(stateMatrix) 
    final_ciphertext+=CipherText 
    IV=CipherText

print("Ciphered Text:")
AES_helper.initial_Print(final_ciphertext.get_bitvector_in_ascii(),1)
EncryptionFinish=time.time()
print()

# BOB received the final ciphertext 
DecryptionStart=time.time()
received_ciphertext = final_ciphertext.get_bitvector_in_ascii()
IV = BitVector(intVal=A, size=128)
final_plaintext=""
for chunk in range(0,chunk_count,1):

    received_cipher=received_ciphertext[16*chunk:16*(chunk+1)]
    stateMatrix=AES_helper.createMatrix(BitVector(textstring=received_cipher))

    stateMatrix = AES_helper.addRoundKey(stateMatrix,AES_helper.createMatrix(roundkeys[10]))
    for iteration in range(9, -1, -1):
        stateMatrix=AES_helper.decryption(stateMatrix,AES_helper.createMatrix(roundkeys[iteration]),iteration)
    result_Plaintext = AES_helper.createBitVector(stateMatrix) 
    result_Plaintext=result_Plaintext^IV
    IV=BitVector(textstring=received_cipher)
    final_plaintext+=result_Plaintext.get_bitvector_in_ascii()

print("Deciphered Text:")
AES_helper.initial_Print(final_plaintext,1)
print()
DecryptionFinish=time.time() 

AES_helper.final_time_print(Key_ScheduingEnd-Key_ScheduingStart , EncryptionFinish-EncryptionStart , DecryptionFinish-DecryptionStart)




