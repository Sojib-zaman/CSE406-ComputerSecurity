from BitVector import * 
import bitvector_demo
import helper

initial_key = "Thats my Kung Fu"
plaintext="Two One Nine Two"

def initial_Print(message):
    print("In ASCII: ",message)
    print("In HEX:",end="")
    for c in message: 
        print(c.encode('utf-8').hex()," ",end=" ")
    print(" ")

def show_hex(w):
    print(w.get_bitvector_in_hex()," ", end="")

def show_matrix(m):
    for i in range(4):
        for j in range(4):
            show_hex(m[i][j])
        print()

def g_operation(w3,round_constant):
    w=w3
    w = w<<8 #circular left shift 
    w=substituteBytes(w)
    w=w^round_constant
    return w 


def createMatrix(bitvector):
    stateMatrix =[]
    for i in range(4):
        row_i = [ ]
        for j in range(4):
            row_i.append(bitvector[(8*i+j*32):(8*i+j*32+8)])
        stateMatrix.append(row_i) 
    return stateMatrix 

def createBitVector(DemoMatrix):
    DemoBitVector=BitVector(size=0)
    for i in range(4):
        for j in range(4):
            DemoBitVector+=DemoMatrix[j][i]
    return DemoBitVector


def addRoundKey(stateMatrix , plainMatrix):
    new_matrix=[]
    for i in range(4):
        row_i = [ ]
        for j in range(4):
            row_i.append(stateMatrix[i][j]^plainMatrix[i][j])
        new_matrix.append(row_i) 
    return new_matrix 

def shiftRow(StateMatrix):
    new_matrix=[]
    for i in range(4):
        row_i = []
        row_bitvector=BitVector(size=0)
        for j in range(4):
            row_bitvector+=StateMatrix[i][j]
        row_bitvector=row_bitvector<<(8*i)
        for k in range(4):
            row_i.append(row_bitvector[8*k:8*(k+1)])
        new_matrix.append(row_i) 
    return new_matrix 



def create_roundkey(key,round_constant):
    w4=key[0:32]^g_operation(key[96:128],round_constant)
    w5=w4^key[32:64] 
    w6=w5^key[64:96]
    w7=w6^key[96:128]
    key=w4+w5+w6+w7
    return key

def substituteBytes(StateMatrix):
    demo_w=BitVector(size=0)
    for i in range(0,StateMatrix.length(),8):
        demo_w+=BitVector(intVal = bitvector_demo.Sbox[StateMatrix[i:i+8].intValue()], size=8)
    return demo_w 

def substituteMatrixBytes(StateMatrix):
    new_matrix=[]
    for i in range(4):
        row_i = [ ]
        for j in range(4):
            row_i.append(BitVector(intVal = bitvector_demo.Sbox[StateMatrix[i][j].intValue()], size=8))
        new_matrix.append(row_i) 
    return new_matrix 

AES_modulus = BitVector(bitstring='100011011')
def MatrixMultiplication(M1,M2):
    new_matrix=[]
    for i in range(4):
        row_i=[]
        for j in range(4):
            x=BitVector(size=0)
            for k in range(4):
                x^=M1[i][k].gf_multiply_modular(M2[k][j],AES_modulus, 8) 
            row_i.append(x)
        new_matrix.append(row_i)
    return new_matrix


print("Key:")
initial_Print(initial_key)



print("Plain Text:")
initial_Print(plaintext)


roundkeys=[]
roundkeys.append(BitVector(textstring=initial_key))
print(roundkeys[0])

print("roundkeys : ")
for i in range(0,10,1): 
    roundkeys.append(create_roundkey(roundkeys[i],helper.round_constant_tuple[i]))
for i in range(0,11,1): 
    show_hex(roundkeys[i])

def encryption(stateMatrix , plainMatrix , iterCount):
    print("After Substitution bytes")
    newStateMatrix = substituteMatrixBytes(stateMatrix) 
    show_matrix(newStateMatrix)
    print("After shift rows")
    newStateMatrix = shiftRow(newStateMatrix)
    show_matrix(newStateMatrix)
    if iterCount!=9 : 
        print("After Mix Columns")
        newStateMatrix=MatrixMultiplication(bitvector_demo.Mixer,newStateMatrix)
        show_matrix(newStateMatrix)
    print("After add round key")
    newStateMatrix = addRoundKey(newStateMatrix , plainMatrix)
    show_matrix(newStateMatrix)
    print()
    return newStateMatrix






print()
stateMatrix = createMatrix(roundkeys[0])
show_matrix(stateMatrix)
plainMatrix = createMatrix(BitVector(textstring=plaintext))
show_matrix(plainMatrix)
print()

print("After add round key")
stateMatrix = addRoundKey(stateMatrix , plainMatrix)
show_matrix(stateMatrix)


for iteration in range (0,10,1):
    print("Round : ",iteration+1) 
    stateMatrix=encryption(stateMatrix,createMatrix(roundkeys[iteration+1]),iteration)
CipherText = createBitVector(stateMatrix) 
show_hex(CipherText)
print()




