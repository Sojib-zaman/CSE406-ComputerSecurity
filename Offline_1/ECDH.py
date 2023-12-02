# y2 = x3 + ax + b , where a and b are public parameters 
# P = 0xfffffffdffffffffffffffffffffffff
# a = 0xfffffffdfffffffffffffffffffffffc
# b = 0xe87579c11079f43dd824993c2cee5ed3
# G = (0x161ff7528b899b2d0c28607ca52c5b86, 0xcf5ac8395bafeb13c02da292dded7a83)
import math 


def ModularInverse(a,p):
    return pow(a,-1,p) 

def point_addition(C,D,P):
    s=( (D[1]-C[1])* ModularInverse( D[0]-C[0] , P ) )%P 
    x3=(s*s-C[0]-D[0])%P
    y3=(s*(C[0]-x3)-C[1])%P
    return (x3,y3)

def point_duplication(G,P):
    s=((3*G[0]*G[0])+a)* ModularInverse(2*G[1],P) 
    s=s%P 
    x3=(s*s-G[0]-G[0])%P
    y3=(s*(G[0]-x3)-G[1])%P
    return (x3,y3)

def scalarMultiplication(a,P,p):
    init=P
    x=1
    binary = format(a,'b')
    print(binary)
    ignore=1
    print(P)
    for bit in binary:
        print("bit ",bit)
        if ignore:
            ignore=0
            continue
        P=point_duplication(P,p)
        x*=2
        print(x,"P ",P)
        if bit=="1" :
            P=point_addition(P,init,p)
            x+=1
            print(x,"P ",P)
    return P 
        


G=(5,1)
P=17
a=2
b=2

#Alice choose his private key as 26 
K_A = 5
Alice_sent_key = scalarMultiplication(K_A, G , P) 

#Bob choose his private key as 15  
K_B = 10
Bob_sent_key = scalarMultiplication(K_B, G , P) 


final_key_for_alice = scalarMultiplication(K_A,Bob_sent_key,P) 
final_key_for_bob = scalarMultiplication(K_B,Alice_sent_key,P) 
print(final_key_for_alice)
print(final_key_for_bob)
