from BitVector import * 
import bitvector_demo
import math
import AES_helper
import time


# initial_key="Thats my Kung Fu"
# given_plaintext="Two One Nine Two"

# initial_key = "BUET CSE19 Batch"
# given_plaintext="Never Gonna Give"


initial_key = "BUET CSE19 Batch"
given_plaintext="Never Gonna Give you up"


chunk_count = math.ceil(len(given_plaintext) / 16)
space_needed= 16*chunk_count- len(given_plaintext) 
for i in range(0,space_needed,1):
    given_plaintext+=" "



print("Key:")
AES_helper.initial_Print(initial_key)



print("Plain Text:")
AES_helper.initial_Print(given_plaintext)



Key_ScheduingStart=time.time()
roundkeys=[]
roundkeys.append(BitVector(textstring=initial_key))
for i in range(0,10,1): 
    roundkeys.append(AES_helper.create_roundkey(roundkeys[i],AES_helper.round_constant_tuple[i]))
Key_ScheduingEnd=time.time()



EncryptionStart=time.time()
final_ciphertext=BitVector(size=0)
IV =  BitVector(textstring="\0")
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

print("Cipher Text:")
AES_helper.initial_Print(final_ciphertext.get_bitvector_in_ascii())
EncryptionFinish=time.time()

# BOB received the final ciphertext 
DecryptionStart=time.time()
received_ciphertext = final_ciphertext.get_bitvector_in_ascii()
IV =  BitVector(textstring="\0")
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

print(final_plaintext)
DecryptionFinish=time.time() 

AES_helper.final_time_print(Key_ScheduingEnd-Key_ScheduingStart , EncryptionFinish-EncryptionStart , DecryptionFinish-DecryptionStart)




