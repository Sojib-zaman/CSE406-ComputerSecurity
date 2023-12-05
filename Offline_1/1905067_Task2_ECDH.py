
# y2 = x3 + ax + b , where a and b are public parameters 
import importlib
bitvector_demo=importlib.import_module("1905067_bitvector_demo")
AES_helper=importlib.import_module("1905067_AES_helper")
ECDH_helper=importlib.import_module("1905067_ECDH_helper")
import Crypto.Util.number
import time 
from prettytable import PrettyTable  



keysize=[128,192,256]
Atimekeeper=[0,0,0]
Btimekeeper=[0,0,0]
Rtimekeeper=[0,0,0]

for ks in range (0,3,1):
    for iteration in range(0,5,1):
        a,b,G,P = ECDH_helper.ECC_param(keysize[ks])




        st=time.time()
        K_A = Crypto.Util.number.getRandomNBitInteger(keysize[ks]) 
        Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a)
        Atimekeeper[ks]+=time.time()-st 
        print("Alice sent key ",Alice_sent_key)


        st=time.time()
        K_B = Crypto.Util.number.getRandomNBitInteger(keysize[ks]) 
        Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a) 
        Btimekeeper[ks]+=time.time()-st 
        print("Bob sent key   ",Bob_sent_key)


        st=time.time()
        final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
        final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
        Rtimekeeper[ks]+=time.time()-st 
        print("Alice final secret key R: ",final_key_for_alice)
        print("Bob final secret key R:   ",final_key_for_bob)



datatable = PrettyTable()
# datatable.field_names=["K" , "Computation Time For"]
# datatable.field_names=[" ", "A" , "B" , "Shared key R"]
datatable.field_names=["K" , "A" , "B" , "R"]
for ks in range(0,3,1):
    datatable.add_row([keysize[ks],Atimekeeper[ks]/5,Btimekeeper[ks]/5,Rtimekeeper[ks]/5])


print(datatable)


