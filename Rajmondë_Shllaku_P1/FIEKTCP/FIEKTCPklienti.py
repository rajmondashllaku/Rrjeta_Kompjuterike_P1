import socket
import sys


def Main():
    serverName = 'localhost'
    serverPort = 13000

    print('Emri i serverit eshte: ' + serverName + ' dhe porti eshte ' + str(serverPort))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName, serverPort))
    print('**********************************************')
    print('*           KOMANDAT E MUNDSHME              *')
    print('1.IPADDRESS \n2.PORT \n3.COUNT \n4.TIME \n5.GAME \n6.REVERSE \n7.CONVERT \n8.GFC \n9.KATRORI \n10.PALINDROME \n11.CAPITALIZE')
    print('***********************************************')
    print('COUNT KA OPSIONET 1.CM TO FEET 2.FEET TO CM 3.KM TO MILES 4.MILES TO KM./nZgjedh numrin 1-4.')
    while True:
        var = input(
            '\nJu lutem shenoni kerkesen: ' + '\n(IPADDRESS, PORT, COUNT, TIME, GAME, REVERSE, CONVERT, GFC, KATRORI, PALINDROME,CAPITALIZE):'
            + '\n -> ')
        s.send(var.encode())
        r = s.recv(1024).decode()

        print('Te dhenat e pranuara nga serveri', r)

        answer = input('A dëshironi të vazhdoni? (PO/JO) -> ')
        if answer.upper() == 'PO':
            continue
        else:
            break
    s.close()


if __name__ == '__main__':
    Main()