import socket 
PORT=8000 

def BobConnection():
    BobSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    BobSocket.bind(('localhost',PORT))
    BobSocket.listen(1)
    while True:
        AliceSocket,AliceAddress=BobSocket.accept()
        #considering only one to one 
        AliceKeys=AliceSocket.recv(1024)
        print("Received : {!r}".format(AliceKeys.decode('utf-8')))
        AliceSocket.sendall(input("Send message ").encode('utf-8'))

if __name__=="__main__":
    BobConnection()
