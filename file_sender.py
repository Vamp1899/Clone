import os, socket
FILE_NAME = 'IMG_4366.jpg'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
client.connect((HOST, PORT))

with open(FILE_NAME, 'rb') as f:
    file_size = os.path.getsize(FILE_NAME)
    # client.send(FILE_NAME.encode('utf-8'))
    # client.send(str(file_size).encode('utf-8'))
    # print(FILE_NAME.encode('utf-8'), str(file_size).encode('utf-8'))
    data = f.read()
    client.sendall(data)
    client.send(b"end")

client.close()