import socket
'''Mention Public IP of server to connect to if not in same LAN '''
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9876

'''This is a TCP socket with socket type as INET'''
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((HOST, PORT))
socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))