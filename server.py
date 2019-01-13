from socket import *
import re

host = 'localhost'
port = 777
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)

print('wait connection...')
conn, addr = tcp_socket.accept()

while True:

    print('client: ', addr)

    data = conn.recv(1024)

    print(data.decode())
    match = re.match(r'[\x00-\x7F]',data.decode())

    if match:
        conn.send('ACK'.encode())
    else:
        conn.send('NACK'.encode())
conn.close()
tcp_socket.close()