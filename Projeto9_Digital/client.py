import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    message = input()
    message = message.encode('utf-8')
    s.send(message)
s.close()

