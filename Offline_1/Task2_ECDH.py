
# y2 = x3 + ax + b , where a and b are public parameters 
import ECDH_helper
import Crypto.Util.number


# a=2
# b=2
# P=19
# G=(5,2)



a,b,G,P = ECDH_helper.ECC_param(128)
# a,b,G,P = 196693035039243160482268747960906501241,210994511040266571180264573151037179426,(233068400230546792194013290862130728026, 279461263148652836855254202426087324532),302835995865414039124360769663136499783
# AliceKey : 9 
# BobKey : 2 

print(a,b,G,P)
#Alice choose his private key as 9
K_A = 9
Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a) 

# #Bob choose his private key as 2  
K_B = 2
Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a) 

print("Alice sent key ",Alice_sent_key)
final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
print(final_key_for_alice)
print(final_key_for_bob)
