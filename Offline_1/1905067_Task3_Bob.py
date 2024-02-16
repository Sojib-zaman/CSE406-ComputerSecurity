import socket 
import json 
import Crypto.Util.number
import importlib
bitvector_demo=importlib.import_module("1905067_bitvector_demo")
AES_helper=importlib.import_module("1905067_AES_helper")
ECDH_helper=importlib.import_module("1905067_ECDH_helper")
from BitVector import *
import math 
Helper = importlib.import_module("1905067_Helper")
PORT=8000 
K_B = Crypto.Util.number.getRandomNBitInteger(128) 
# print("kb ",K_B)
#K_B = 335219312588335512351205011508989133212

def BobConnection():
    BobSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    BobSocket.bind(('localhost',PORT))
    BobSocket.listen(1)
    while True:
        AliceSocket,AliceAddress=BobSocket.accept()
        #considering only one to one 


        AliceKeys=AliceSocket.recv(1024)
        received_data = json.loads(AliceKeys.decode('utf-8'))
        a,b,G,Alice_sent_key,P=received_data
        print("Received from Alice : ")
        print(Helper.TextStyle.BOLD,Helper.TextColor.CYAN)
        print("a : ",a,"\nb: ",b, "\npoint G : ", G , "\nK_a*g(mod P) : ",Alice_sent_key , "\nPrime P : ",P,Helper.TextStyle.RESET)
        
        
        
        
        Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a)     
        Bob_sent_key=json.dumps(Bob_sent_key) 
        AliceSocket.sendall(Bob_sent_key.encode('utf-8'))
        
        
        
        
        final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
        #print("The final key for Bob : ",final_key_for_bob)

        print(AliceSocket.recv(1024).decode('utf-8'))
        message="BOB sent : Bob ready for transmission"
        AliceSocket.sendall(message.encode('utf-8'))


        shared_secret_key=final_key_for_bob[0]
        print(Helper.TextStyle.BOLD,Helper.TextColor.MAGENTA)
        print("Shared Secret Key : " , shared_secret_key,Helper.TextStyle.RESET)

        
        received_ciphertext=AliceSocket.recv(1024).decode('utf-8')



        print("Received the IVciphertext from alice : ")
 
        IV=received_ciphertext[:16]
        IV=BitVector(textstring=IV)
        # 
        received_ciphertext=received_ciphertext[16:]
        print(Helper.TextStyle.BOLD,Helper.TextColor.YELLOW)
        print("received ciphertext : ",received_ciphertext,Helper.TextStyle.RESET)
     
        bin_shared = AES_helper.bitkeychecker(shared_secret_key)
        roundkeys=[]
        roundkeys.append(BitVector(bitstring=bin_shared))
        for i in range(0,10,1): 
            roundkeys.append(AES_helper.create_roundkey(roundkeys[i],AES_helper.round_constant_tuple[i]))   

        
        final_plaintext=""
        chunk_count = math.ceil(len(received_ciphertext) / 16)
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
        break
    AliceSocket.close()
    BobSocket.close()

        
        

if __name__=="__main__":
    BobConnection()
