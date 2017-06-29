import socket
from datetime import datetime


if __name__ == '__main__':
    server = "192.168.1.173"
    recf = ('', 7091)
    send_to = (server, 7090)

    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    reciver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    reciver.bind(recf)
    while True:
        message = input('send: ').encode('utf-8')
        sender.sendto(message, send_to)
        data, addr = reciver.recvfrom(1024)
        print('{t}: response: {d}\n'.format(t = datetime.now(), d = data.decode('utf-8')))
