import socket 
import json 
import ECDH_helper
PORT=8000 
K_B=2
def BobConnection():
    BobSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    BobSocket.bind(('localhost',PORT))
    BobSocket.listen(1)
    while True:
        AliceSocket,AliceAddress=BobSocket.accept()
        #considering only one to one 
        AliceKeys=AliceSocket.recv(1024)
        received_data = json.loads(AliceKeys.decode('utf-8'))
        a,b,G,Alice_sent_key,P=received_data
        print("a : ",a," b: ",b, " point G : ", G , " K_a*g(mod P) : ",Alice_sent_key , " Prime P : ",P)
        Bob_sent_key = ECDH_helper.scalarMultiplication(K_B, G , P,a)     
        Bob_sent_key=json.dumps(Bob_sent_key) 
        AliceSocket.sendall(Bob_sent_key.encode('utf-8'))
        final_key_for_bob = ECDH_helper.scalarMultiplication(K_B,Alice_sent_key,P,a) 
        print("The final key for Bob : ",final_key_for_bob)

if __name__=="__main__":
    BobConnection()
