import socket 

PORT=8000 

def AliceConnection():
    AliceSocket=socket.socket(socket.AF_INET ,socket.SOCK_STREAM )
    AliceSocket.connect(('localhost',PORT))

    while True: 
        AliceSocket.sendall(input("Send message ").encode('utf-8'))
        BobKeys=AliceSocket.recv(1024)
        print("Received : {!r}".format(BobKeys.decode('utf-8')))
        
if __name__=="__main__":
    AliceConnection()


