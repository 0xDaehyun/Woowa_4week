from socket import *;
import threading;

clients = []

port = 8080
serverSock = socket(AF_INET , SOCK_STREAM) # 소켓을 생성 (어드레스 패밀리 , 소켓 타입의 인자) 가 필요하다.
serverSock.bind(('', port))
# 바인드는 소켓과 AF를 연결하는 과정. 이 인자는 어드레스 패밀리가 된다
# 클라이언트를 만들떄는 불필요하며. 서버를 운용할떄는 반드시 필요하다.
# ' ' 으로 주소에 해당되는 부분을 비워놓는 이유는 모든 인터페이스를 연결한다는 뜻이다.
# 브로드캐스트를 하고 싶다면 '' 으로 !
serverSock.listen(3)
#상대방의 접속을 기다리겠다는 뜻이더.
print('%d번 포트로 접속 대기중...'%port)
connectionSock, addr = serverSock.accept()
# 누군가가 접속하여 연결 하였을 때에 비로소 결과값이 return 되는 함수이다.
# return 값으로 (새로운 소켓, 상대방의 AF)를 전달해주게 됩니다.

def handle_client(connectionSock, addr):
    print(str(addr) , '에서 접속됐습니다.')

    while True:
        data = connectionSock.recv(1024)
        msg = data.decode('utf-8')
        print('받은 메시지:', msg)

        # 받은 메시지를 다른 클라이언트들에게 브로드캐스트
        for c in clients:
            if c is not connectionSock:
                    c.send(msg.encode('utf-8'))


# 여러 클라이언트 접속 받기
while True:
    connectionSock, addr = serverSock.accept()
    # 누군가가 접속하여 연결 하였을 때에 비로소 결과값이 return 되는 함수이다.
    # return 값으로 (새로운 소켓, 상대방의 AF)를 전달해주게 됩니다.

    clients.append(connectionSock)

    t = threading.Thread(target=handle_client, args=(connectionSock, addr))
    t.daemon = True
    t.start()