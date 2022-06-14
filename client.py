from http import client
from pydoc import cli
import socket

#서버 IP & Port 
server_ip = '127.0.0.1'
port = 9999

#클라이언트 소켓 준비
client = socket.socket()

#서버 접속
client.connect((server_ip, port))
print('----- Server is connect -----')

#메세지 입력
print("이름을 입력하세요(ex: Jang) :")
msg = input()

#메세지 송신
client.send(bytes(msg, 'utf-8'))
print('----- Message send -----')

#메세지 수신
msg = client.recv(1024)
print('----- Message received ------')
print(msg)

client.close()