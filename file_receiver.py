import socket, tqdm
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
server.bind((HOST, PORT))
server.listen()
client, addr = server.accept()
# file_name = client.recv(1024).decode('utf-8')
# file_size = client.recv(1024).decode('utf-8')
file_bytes = b""
done = False
# progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=file_size)
while True:
    data = client.recv(1024)
    if data.endswith(b"end"):
        file_bytes += data[:-3]  # Append data without the "end" bytes
        break
    file_bytes += data
    # progress.update(len(data))

with open('passport_copy.jpeg', 'wb') as f:
    f.write(file_bytes)

server.close()
