import socket

HOST = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 2048

sockC = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockC.connect((HOST,PORT))
try:
    message = 'hello'
    #明天再搞
    sockC.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:

        data=sockC.recv(1024)
        amount_received +=len(data)
    print("C Received {}".format(data.decode()))
except Exception as e:
    print(e)
finally:
    print("closing connection")
    sockC.close()
