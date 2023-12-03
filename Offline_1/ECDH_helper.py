import math 


def ModularInverse(a,p):
    return pow(a,-1,p) 

def point_addition(C,D,P):
    s=( (D[1]-C[1])* ModularInverse( D[0]-C[0] , P ) )%P 
    x3=(s*s-C[0]-D[0])%P
    y3=(s*(C[0]-x3)-C[1])%P
    return (x3,y3)

def point_duplication(G,P,a):
    s=((3*G[0]*G[0])+a)* ModularInverse(2*G[1],P) 
    s=s%P 
    x3=(s*s-G[0]-G[0])%P
    y3=(s*(G[0]-x3)-G[1])%P
    return (x3,y3)

def scalarMultiplication(a,P,p,g_a):
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
        P=point_duplication(P,p,g_a)
        x*=2
        print(x,"P ",P)
        if bit=="1" :
            P=point_addition(P,init,p)
            x+=1
            print(x,"P ",P)
    return P 
        

