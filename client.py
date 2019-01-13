from socket import *

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)
sum=3

while True:
    data = input('Напишите серверу (только ASCII символы): ')

    tcp_socket.send(data.encode())

    data = tcp_socket.recv(1024)
    print('Ответ сервера: ',data.decode())

    if data.decode()=='NACK':
        sum-=1
        print('Количество оставшихся попыток: ', sum)

    if sum==0:
        print('Попытки закончились. Ваш сеанс завершен')
        break


tcp_socket.close()
