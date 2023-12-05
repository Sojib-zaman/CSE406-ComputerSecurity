import math 
import Crypto.Util.number

def EuclidGCD(a,p):
    if p==0 : 
        return a 
    else : 
        return EuclidGCD(p,a%p)
    

def fermat(a,pow,prime):
    if pow==0:
        return 1
    retval = fermat(a,pow//2,prime)%prime
    retval = (retval**2)%prime 
    if pow%2==0:
        return retval 
    else :
        return (a*retval)%prime 
    
def ModularInverse(a,p):
    if EuclidGCD(a,p)==1:
        return fermat(a,p-2,p)
          


def point_addition(C,D,P):
    s=( (D[1]-C[1])* ModularInverse( D[0]-C[0] , P ) )%P 
    x3=(s*s-C[0]-D[0])%P
    y3=(s*(C[0]-x3)-C[1])%P
    return (x3,y3)

def point_duplication(G,prime,a):
    #print(G,prime,a)
    s=((3*G[0]*G[0])+a)*ModularInverse(2*G[1],prime) 
    #print(s)
    s=s%prime
    #print(s)
    x3=(s*s-G[0]-G[0])%prime
    y3=(s*(G[0]-x3)-G[1])%prime
    return (x3,y3)

# SecretKey , Point , Prime , GraphParameterA
def scalarMultiplication(a,P,p,g_a):
    init=P
    current_XP=1
    binary = format(a,'b')
    #print(binary)
    ignore=1
    #print(P)
    for bit in binary:
        #print("bit ",bit)
        if ignore:
            ignore=0
            continue
        P=point_duplication(P,p,g_a)
        current_XP*=2
        #print(current_XP,"P ",P)
        if bit=="1" :
            P=point_addition(P,init,p)
            current_XP+=1
            #print(current_XP,"P ",P)
    return P 



# y2 = x3 + ax + b 
#then b = y2-x3-ax 
def ECC_param(keySize):
    condition = True 
    while condition:
        a=Crypto.Util.number.getRandomNBitInteger(keySize) 
        G=(Crypto.Util.number.getRandomNBitInteger(keySize),Crypto.Util.number.getRandomNBitInteger(keySize))
        p=Crypto.Util.number.getPrime(keySize) 
        a=a%p
        b=G[1]**2-a*G[0]-G[0]**3 
        b=b%p

        if (4*(a**3) + 27*(b**2))%p != 0:
            condition=False
    return a,b,G,p 






    


