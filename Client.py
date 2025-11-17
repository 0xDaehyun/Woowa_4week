from socket import *;
import threading;

def send(sock):
 while True:
    sendData = input('>>>')
    sock.send(sendData.encode('utf-8'))

def recv(sock):
 while True:
    recieveData = sock.recv(1024)
    print('상대방 :' ,recieveData.decode('utf-8'))

port  = 8080

clientSock = socket(AF_INET , SOCK_STREAM)  # 서버와 연결할 소켓 객체를 생성
clientSock.connect(('127.0.0.1' , port)) #ip주소와 port 번호로 서버와 연결을 요청해 수락을 기다린다 .

# 127.0.0.1은 자기 자신을 의미한다.
# 위의 어드레스 패밀리는 자기 자신에게 8080번 포트로 연결하란 소리가 되겠네요.

print('서버와 연결 완료!')

sendTread = threading.Thread(target=send , args=(clientSock, ))
receiver = threading.Thread(target=recv , args=(clientSock, ))

sendTread.start()
receiver.start()

sendTread.join()
receiver.join()