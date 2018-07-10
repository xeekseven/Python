import socket

HOST = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 1024

sockS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockS.bind((HOST,PORT))

sockS.listen(5)

print("Server Start")

conn,addr = sockS.accept()
data = conn.recv(BUFFER_SIZE)
if len(data):
    print('Server recev Data {}'.format(data.decode()))
    conn.send(data)
    print("server send data")

while True:
    conn,addr = sockS.accept()
    while True:
        data = conn.recv(BUFFER_SIZE)
        if len(data):
            print('Server Recv Data:{}'.format(data))
            conn.send(data)
            print('Server Recved so send Data:{}'.format(data))
        else:
            print('Server Recv Over')
            break
    conn.close()
sockS.close()
