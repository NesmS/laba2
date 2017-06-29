import socket
from datetime import datetime

def handler(byte_data):
    data = byte_data.decode('utf-8')
    ret = ''
    if data == 'time':
        ret = str(datetime.now())
    elif data[-5:] == '#caps':
        ret = data[:-5].upper()
    else:
        ret = str(len(data))
    return ret.encode('utf-8')


if __name__ == '__main__':
    client = "192.168.1.38"
    recf = ('', 7090)
    send_to = (client, 7091)

    reciver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    reciver.bind(recf)
    while True:
        data, addr = reciver.recvfrom(1024)
        print('{t}: message: {d}'.format(t = datetime.now(), d = data.decode('utf-8')))
        sender.sendto(handler(data), send_to)