#2020 01 10
#visual studio code python 3.8.1

import socket # 소켓모듈 import

#소켓 생성
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   

#문자열 서버에 보내기

client.sendto("Test".encode(),('100.1.50.120',7878))

#텔로드론을 사용하기 위해서 기본적인 소켓 공부.
#처음 클라이언트와 서버 통신을 테스트하는 것이기 때문에 코드가 간단함.
