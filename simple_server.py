import socket

'''Get Private IP without virtual box'''
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9876
print(HOST)
'''This is a TCP socket with socket type as INET'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''Server socket is just used for accepting connection request'''
server.bind((HOST, PORT))
'''Waiting queue length for connections'''
server.listen(5)

while True:
    '''Clients socket is used for communication not the server one'''
    com_socket, addr = server.accept()
    print(f"Connected to {addr} ")
    '''Byte streams not strings'''
    message = com_socket.recv(1024).decode('utf-8')
    print(f'Message from client is {message}')
    com_socket.send(f"Got your message - {message}, Thank!".encode('utf-8'))
    print(f'Connection with {addr} ended!')
    if com_socket.close() == None:
        break
