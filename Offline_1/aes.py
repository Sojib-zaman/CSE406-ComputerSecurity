from BitVector import * 
import bitvector_demo
import helper
import math

def initial_Print(message):
    print("In ASCII: ",message)
    print("In HEX:",end="")
    for c in message: 
        #print(c.encode('utf-8').hex()," ",end=" ")
        print("{0:02x}".format(ord(c),"x"),end=" ")
    print(" ")

def show_hex(w):
    print(w.get_bitvector_in_hex()," ", end="")

def show_ascii(w):
    print(w.get_bitvector_in_ascii()," ", end="")



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

def InvShiftRow(StateMatrix):
    new_matrix=[]
    for i in range(4):
        row_i = []
        row_bitvector=BitVector(size=0)
        for j in range(4):
            row_bitvector+=StateMatrix[i][j]
        row_bitvector=row_bitvector>>(8*i)
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

def InverseSubstituteMatrixBytes(StateMatrix):
    new_matrix=[]
    for i in range(4):
        row_i = [ ]
        for j in range(4):
            row_i.append(BitVector(intVal = bitvector_demo.InvSbox[StateMatrix[i][j].intValue()], size=8))
        new_matrix.append(row_i) 
    return new_matrix 
    
AES_modulus = BitVector(bitstring='100011011')
# Matrix Multiplication is basically mix columns and inverse (based on the first matrix )
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





def encryption(stateMatrix , plainMatrix , iterCount):
    newStateMatrix = substituteMatrixBytes(stateMatrix) 
    newStateMatrix = shiftRow(newStateMatrix)
    if iterCount!=9 : 
        newStateMatrix=MatrixMultiplication(bitvector_demo.Mixer,newStateMatrix)
    newStateMatrix = addRoundKey(newStateMatrix , plainMatrix)
    return newStateMatrix

def decryption(stateMatrix , plainMatrix , iterCount):
    newStateMatrix=InvShiftRow(stateMatrix) 
    newStateMatrix=InverseSubstituteMatrixBytes(newStateMatrix)
    newStateMatrix=addRoundKey(newStateMatrix , plainMatrix)
    if iterCount!=0:
        newStateMatrix=MatrixMultiplication(bitvector_demo.InvMixer,newStateMatrix)
    return newStateMatrix






# initial_key="Thats my Kung Fu"
# given_plaintext="Two One Nine Two"

# initial_key = "BUET CSE19 Batch"
# given_plaintext="Never Gonna Give"


initial_key = "BUET CSE19 Batch"
given_plaintext="Never Gonna Give you up"


chunk_count = math.ceil(len(given_plaintext) / 16)
space_needed= 16*chunk_count- len(given_plaintext) 
for i in range(0,space_needed,1):
    given_plaintext+=" "



print("Key:")
initial_Print(initial_key)



print("Plain Text:")
initial_Print(given_plaintext)


roundkeys=[]
roundkeys.append(BitVector(textstring=initial_key))



for i in range(0,10,1): 
    roundkeys.append(create_roundkey(roundkeys[i],helper.round_constant_tuple[i]))





final_ciphertext=BitVector(size=0)
IV =  BitVector(textstring="\0")
for chunk in range(0,chunk_count,1):
    plaintext=given_plaintext[16*chunk:16*(chunk+1)]
    plaintext = BitVector(textstring=plaintext)^IV 
    stateMatrix = createMatrix(roundkeys[0])
    plainMatrix = createMatrix(plaintext)
    stateMatrix = addRoundKey(stateMatrix , plainMatrix)
    for iteration in range (0,10,1):
        stateMatrix=encryption(stateMatrix,createMatrix(roundkeys[iteration+1]),iteration)
    CipherText = createBitVector(stateMatrix) 
    final_ciphertext+=CipherText 
    IV=CipherText

print("Cipher Text:")
initial_Print(final_ciphertext.get_bitvector_in_ascii())


# BOB received the final ciphertext 

received_ciphertext = final_ciphertext.get_bitvector_in_ascii()
IV =  BitVector(textstring="\0")
final_plaintext=""
for chunk in range(0,chunk_count,1):

    received_cipher=received_ciphertext[16*chunk:16*(chunk+1)]
    stateMatrix=createMatrix(BitVector(textstring=received_cipher))

    stateMatrix = addRoundKey(stateMatrix,createMatrix(roundkeys[10]))
    for iteration in range(9, -1, -1):
        stateMatrix=decryption(stateMatrix,createMatrix(roundkeys[iteration]),iteration)
    result_Plaintext = createBitVector(stateMatrix) 
    result_Plaintext=result_Plaintext^IV
    IV=BitVector(textstring=received_cipher)
    final_plaintext+=result_Plaintext.get_bitvector_in_ascii()

print(final_plaintext)





