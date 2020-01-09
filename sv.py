#2020 01 10 
#visual studio code python 3.8.1

import socket

#소켓 생성
server = socket(AF_INET,SOCK_DGRAM) 

#서버 아이피 ,포트번호 고정
server.bind(('192.168.1.1',7777))

#수신가능한 최대 크기 100byte, 반환값  
data, address = server.recvfrom(100) 

print("서버가 받는 데이터:",data.decode())

print("보내온 아이피:",address[0])

print("보내온 포트번호:",address[1])
