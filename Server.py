from socket import *;

serverSock = socket(AF_INET , SOCK_STREAM)
# 소켓 객체를 생성할때는 어드레스 패밀리 , 소켓 타입의 인자를 두개 받아야 한다

serverSock.bind(('', 8080))
# 바인드는 소켓과 AF를 연결하는 과정이라 했다. 이 인자는 어드레스 패밀리가 된다
# 클라이언트를 만들떄는 불필요하며. 서버를 운용할떄는 반드시 필요하다.
# ' ' 으로 주소에 해당되는 부분을 비워놓는 이유는 모든 인터페이스를 연결한다는 뜻이다.
#브로드캐스트를 하고 싶다면 '' 으로 !
serverSock.listen(1)
#상대방의 접속을 기다리겠다는 뜻이더.

connectionSock, addr = serverSock.accept()
# 누군가가 접속하여 연결 하였을 때에 비로소 결과값이 return 되는 함수이다.
# return 값으로 새로운 소켓과, 상대방의 AF를 전달해주게 됩니다.


print(str(addr) , '에서 접속이 확인되었습니다')
data = connectionSock.recv(1024)
print('받은 데이터: ' , data.decode('utf-8'))

connectionSock.send('서버에서 보낸다! '.encode('utf-8'))
print('서버에서 메시지 전송 완료')