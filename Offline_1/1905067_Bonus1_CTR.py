from BitVector import * 
import importlib
bitvector_demo=importlib.import_module("1905067_bitvector_demo")
AES_helper=importlib.import_module("1905067_AES_helper")
import time
import math
import Crypto.Util.number
import threading 
# initial_key = "BUET CSE19 Batch"
# given_plaintext="Never gonna givw you up. THERE IS SOMETHING HAPPENING"


initial_key=input("Input a 128 bit key : ")
initial_key = AES_helper.keychecker(initial_key)
print("Key:")
AES_helper.initial_Print(initial_key)
print()
given_plaintext=input("Input the plaintext to be sent : ")




def encryptionThread(chunk_iter  , plaintext ,  IV , roundkeys):
    #print(chunk_iter," ", plaintext , " ", IV) 
    plainMatrix = AES_helper.createMatrix(IV)
    stateMatrix = AES_helper.createMatrix(roundkeys[0])
    stateMatrix = AES_helper.addRoundKey(stateMatrix , plainMatrix)
    for iteration in range (0,10,1):
        stateMatrix=AES_helper.encryption(stateMatrix,AES_helper.createMatrix(roundkeys[iteration+1]),iteration)
    CipherText = AES_helper.createBitVector(stateMatrix)
    CipherText=CipherText^BitVector(textstring=plaintext)
    enc_output[chunk_iter]=CipherText.get_bitvector_in_ascii()




def decryptionThread(chunk_iter  , ciphertext ,  IV , roundkeys):
    plainMatrix = AES_helper.createMatrix(IV)
    stateMatrix = AES_helper.createMatrix(roundkeys[0])
    stateMatrix = AES_helper.addRoundKey(stateMatrix , plainMatrix)
    for iteration in range (0,10,1):
        stateMatrix=AES_helper.encryption(stateMatrix,AES_helper.createMatrix(roundkeys[iteration+1]),iteration)
    encOut = AES_helper.createBitVector(stateMatrix)
    plaintext=encOut^BitVector(textstring=ciphertext)
    dec_output[chunk_iter]=plaintext.get_bitvector_in_ascii()


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
A=304795977167082282169655249262004358764
IV = BitVector(intVal=A, size=128)
chunk_count = math.ceil(len(given_plaintext) / 16)

enc_output=[""]*chunk_count
dec_output=[""]*chunk_count


threads=[]
for chunk in range(0,chunk_count,1):
    plaintext=given_plaintext[16*chunk:16*(chunk+1)]
    thread=threading.Thread(target=encryptionThread, args=(chunk,plaintext,IV,roundkeys))
    XIv = IV.intValue()
    XIv+=1
    IV = BitVector(intVal=XIv, size=128)
    threads.append(thread)


for t in threads:
    t.start()

for t in threads:
    t.join()  

print("Ciphered Text:")
received_cipher=""
for x in enc_output:
    received_cipher+=x 
print(received_cipher)


EncryptionFinish=time.time()
print()

DecryptionStart=time.time()
IV = BitVector(intVal=A, size=128)
decthreads=[]
for chunk in range(0,chunk_count,1):
    ciphertext=received_cipher[16*chunk:16*(chunk+1)]
    thread=threading.Thread(target=decryptionThread, args=(chunk,ciphertext,IV,roundkeys))
    XIv = IV.intValue()
    XIv+=1
    IV = BitVector(intVal=XIv, size=128)
    decthreads.append(thread)

for t in decthreads:
    t.start()

for t in decthreads:
    t.join()   

Deciphered_text=""
for x in dec_output:
    Deciphered_text+=x 




print("Deciphered Text:")
AES_helper.initial_Print(Deciphered_text,1)
print()
DecryptionFinish=time.time() 

AES_helper.final_time_print(Key_ScheduingEnd-Key_ScheduingStart , EncryptionFinish-EncryptionStart , DecryptionFinish-DecryptionStart)




# for chunk in range(0,chunk_count,1):
#     plaintext=given_plaintext[16*chunk:16*(chunk+1)]
#     plainMatrix = AES_helper.createMatrix(IV)
#     stateMatrix = AES_helper.createMatrix(roundkeys[0])
#     stateMatrix = AES_helper.addRoundKey(stateMatrix , plainMatrix)
#     for iteration in range (0,10,1):
#         stateMatrix=AES_helper.encryption(stateMatrix,AES_helper.createMatrix(roundkeys[iteration+1]),iteration)
#     CipherText = AES_helper.createBitVector(stateMatrix)
#     CipherText=CipherText^BitVector(textstring=plaintext)
#     final_ciphertext+=CipherText 
#     XIv = IV.intValue()
#     XIv+=1
#     IV = BitVector(intVal=XIv, size=128)

# print("Ciphered Text:")
# AES_helper.initial_Print(final_ciphertext.get_bitvector_in_ascii(),1)
# EncryptionFinish=time.time()
# print()

# # BOB received the final ciphertext 
# DecryptionStart=time.time()
# received_ciphertext = final_ciphertext.get_bitvector_in_ascii()
# IV = BitVector(intVal=A, size=128)
# final_plaintext=""

# for chunk in range(0,chunk_count,1):
#     CipherText=received_ciphertext[16*chunk:16*(chunk+1)]
#     plainMatrix = AES_helper.createMatrix(IV)
#     stateMatrix = AES_helper.createMatrix(roundkeys[0])
#     stateMatrix = AES_helper.addRoundKey(stateMatrix , plainMatrix)
#     for iteration in range (0,10,1):
#         stateMatrix=AES_helper.encryption(stateMatrix,AES_helper.createMatrix(roundkeys[iteration+1]),iteration)
#     encOut = AES_helper.createBitVector(stateMatrix)
#     plaintext=encOut^BitVector(textstring=CipherText)
#     final_plaintext+=plaintext.get_bitvector_in_ascii() 
#     XIv = IV.intValue()
#     XIv+=1
#     IV = BitVector(intVal=XIv, size=128)



    

# print("Deciphered Text:")
# AES_helper.initial_Print(final_plaintext,1)
# print()
# DecryptionFinish=time.time() 

# AES_helper.final_time_print(Key_ScheduingEnd-Key_ScheduingStart , EncryptionFinish-EncryptionStart , DecryptionFinish-DecryptionStart)




