#2020 01 10
#visual studio code python 3.8.1

import socket # 소켓모듈 import

#소켓 생성
client = socket(AF_INET,SOCK_DGRAM)   

#문자열 서버에 보내기

client.sendto("Test".encode(),('100.1.50.120',7878))