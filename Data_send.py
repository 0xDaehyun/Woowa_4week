def send(sock):
 while True:
    sendData = input('>>>')
    sock.send(sendData.encode('utf-8'))