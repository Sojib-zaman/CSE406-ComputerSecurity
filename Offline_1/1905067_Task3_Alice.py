import socket 
import json 
import Crypto.Util.number
import math
import importlib
bitvector_demo=importlib.import_module("1905067_bitvector_demo")
AES_helper=importlib.import_module("1905067_AES_helper")
ECDH_helper=importlib.import_module("1905067_ECDH_helper")
from BitVector import *
import sys
Helper = importlib.import_module("1905067_Helper")


PORT=8000 

a,b,G,P = ECDH_helper.ECC_param(128)
# print(a,b,G,P)
K_A = Crypto.Util.number.getRandomNBitInteger(128) 
# print("KA ",K_A)

# G=[323392595161789581893682962851819092925, 192001708202558040940461988175842556465]
# P=200513256155358798247572125315957745259
# a=54092382098935824204905395252435751400
# b=34183678491666029866491825370341452117
# K_A = 258284983278789018511670191847474482444

def AliceConnection():
    AliceSocket=socket.socket(socket.AF_INET ,socket.SOCK_STREAM )
    AliceSocket.connect(('localhost',PORT))



    Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a) 
    # print("Alice sent key : ")
    # print(Alice_sent_key)
    Alice_data = (a,b,G,Alice_sent_key,P)
    Alice_data=json.dumps(Alice_data)
    
    while True: 
        AliceSocket.sendall(Alice_data.encode('utf-8'))
        Bob_sent_key=AliceSocket.recv(1024).decode('utf-8')
        Bob_sent_key = json.loads(Bob_sent_key)
        Bob_sent_key = tuple(Bob_sent_key)
        #print("BOb sent key : ",Bob_sent_key) 
        

        final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
        #print("The final key for Alice : ",final_key_for_alice)




        message="ALICE sent : Alice ready for transmission"
        AliceSocket.sendall(message.encode('utf-8'))
        print(AliceSocket.recv(1024).decode('utf-8'))



        shared_secret_key=final_key_for_alice[0]
        print(Helper.TextStyle.BOLD,Helper.TextColor.MAGENTA)
        print("Shared Secret Key : " , shared_secret_key,Helper.TextStyle.RESET)

        given_plaintext=input("Input the plaintext to be sent : ")
        given_plaintext=AES_helper.plaintextchecker(given_plaintext)
        
        print("Plain Text:")
        AES_helper.initial_Print(given_plaintext)
        print()
        size_of_x_in_bits = int(math.log2(shared_secret_key)) + 1
        #print("Size of shared secret key : ", size_of_x_in_bits)
        bin_shared = AES_helper.bitkeychecker(shared_secret_key)

        roundkeys=[]
        roundkeys.append(BitVector(bitstring=bin_shared))
        for i in range(0,10,1): 
            roundkeys.append(AES_helper.create_roundkey(roundkeys[i],AES_helper.round_constant_tuple[i]))
        
        final_ciphertext=BitVector(size=0)
        A=Crypto.Util.number.getRandomNBitInteger(128) 
        IV = BitVector(intVal=A, size=128)
        #print("IV : ", IV.get_bitvector_in_ascii())
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

        IV = BitVector(intVal=A, size=128)
        final_bitvector = IV+final_ciphertext 
        final_message_from_alice = final_bitvector.get_bitvector_in_ascii()
        # print(final_message_from_alice)
 
        
        AliceSocket.sendall(final_message_from_alice.encode('utf-8'))
        break 
        
if __name__=="__main__":
    AliceConnection()


