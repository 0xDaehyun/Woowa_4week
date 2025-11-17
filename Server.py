from socket import *;

serverSock = socket(AF_INET , SOCK_STREAM)

serverSock.bind(('', 8080))
# 클라이언트를 만들떄는 불필요하며.
# 서버를 운용할떄는 반드시 필요하다.
#'' 으로 주소에 해당되는 부분을 비워놓는 이유는 모든 인터페이스를 연결한다는 뜻이다.
#브로드캐스트를 하고 싶다면 '' 으로 !
serverSock.listen(1)
#
connectionSoc, addr = serverSock.accept()
# 누군가가 접속하여 연결 하였을 때에 비로소 결과값이 return 되는 함수이다.

print(str(addr) , '에서 접속이 확인되었습니다')
data = connectionSoc.recv(1024)


 