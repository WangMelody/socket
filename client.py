import socket

HOST = '127.0.0.1'
PORT = 8000


while True:
    # clientMessage = 'Hello!'
    clientMessage = input('self : ')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())

    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server replied:', serverMessage)

client.close()      