# y2 = x3 + ax + b , where a and b are public parameters 
import ECDH_helper
import Crypto.Util.number
G=(5,1)
P=17
a=2
b=2



#Alice choose his private key as 9
K_A = 9
Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a) 

#Bob choose his private key as 2  
K_B = 2
Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a) 


final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
print(final_key_for_alice)
print(final_key_for_bob)
