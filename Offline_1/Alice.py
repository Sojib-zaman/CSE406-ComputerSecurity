import socket 
import ECDH_helper
import json 
PORT=8000 

G=(5,1)
P=17
a=2
b=2
K_A=9



def AliceConnection():
    AliceSocket=socket.socket(socket.AF_INET ,socket.SOCK_STREAM )
    AliceSocket.connect(('localhost',PORT))
    Alice_sent_key = ECDH_helper.scalarMultiplication(K_A, G , P,a) 
    Alice_data = (a,b,G,Alice_sent_key,P)
    Alice_data=json.dumps(Alice_data)
    
    while True: 
        AliceSocket.sendall(Alice_data.encode('utf-8'))
        Bob_sent_key=AliceSocket.recv(1024)
        final_key_for_alice = ECDH_helper.scalarMultiplication(K_A,Bob_sent_key,P,a) 
        print("The final key for Alice : ",final_key_for_alice)
        
if __name__=="__main__":
    AliceConnection()


