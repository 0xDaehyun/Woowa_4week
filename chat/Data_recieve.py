def recv(sock):
 while True:
    recieveData = sock.recv(1024)
    print('상대방 :' ,recieveData.decode('utf-8'))