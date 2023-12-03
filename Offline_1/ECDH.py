# y2 = x3 + ax + b , where a and b are public parameters 
# P = 0xfffffffdffffffffffffffffffffffff
# a = 0xfffffffdfffffffffffffffffffffffc
# b = 0xe87579c11079f43dd824993c2cee5ed3
# G = (0x161ff7528b899b2d0c28607ca52c5b86, 0xcf5ac8395bafeb13c02da292dded7a83)
import ECDH_helper

G=(5,1)
P=17
a=2
b=2

#Alice choose his private key as 26 
K_A = 5
Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a) 

#Bob choose his private key as 15  
K_B = 10
Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a) 


final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
print(final_key_for_alice)
print(final_key_for_bob)
