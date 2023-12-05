# y2 = x3 + ax + b , where a and b are public parameters 
import ECDH_helper
import Crypto.Util.number
G=[323392595161789581893682962851819092925, 192001708202558040940461988175842556465]
P=200513256155358798247572125315957745259
a=54092382098935824204905395252435751400
b=34183678491666029866491825370341452117



#Alice choose his private key as 9
K_A = 258284983278789018511670191847474482444
Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a) 
print("ALice sent : ",Alice_sent_key)

#Bob choose his private key as 2  
K_B = 335219312588335512351205011508989133212
Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a) 
print("Bob sent key : ",Bob_sent_key)


final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
print(final_key_for_alice)
print(final_key_for_bob)
