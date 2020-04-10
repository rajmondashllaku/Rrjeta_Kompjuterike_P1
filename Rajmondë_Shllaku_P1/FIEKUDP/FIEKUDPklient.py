import socket
import sys

#serverAddressPort  = ("localhost", 13000)

serverName = "localhost"
port = 13000

print('Emri i serverit eshte: ' + serverName + ' dhe porti eshte ' + str(port))


serverAddressPort = (serverName, port)

print('**********************************************')
print('*           KOMANDAT E MUNDSHME              *')
print(
    '1.IPADDRESS \n2.PORT \n3.COUNT \n4.TIME \n5.TIME \n6.GAME \n7.REVERSE \n8.CONVERT \n9.GFC \n10.KATRORI \n11.PALINDROME \n12.CAPITALIZE')
print('***********************************************')
print('COUNT KA ZGJEDHJET 1.CMTOFEET 2.FEETTOCM 3.KMTOMILES 4.MILESTOKM.\nZgjedh opsionin.')


UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    var = input(
        '\nJu lutem shenoni kerkesen: ' + '\n(IPADDRESS, PORT, COUNT, TIME, GAME, REVERSE, CONVERT, GFC, KATRORI, PALINDROME, CAPITALIZE):'
        + '\n -> ')

    var = str.encode(var)

    UDPClientSocket.sendto(var, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(1024)

    msg = "Te dhenat e pranuara nga serveri: {}".format(msgFromServer[0].decode())

    print(msg)

    pergjegja = input('A dëshironi të vazhdoni? (PO/JO) -> ')

    if pergjegja.upper() == 'PO':
        continue
    elif pergjegja.upper() == 'JO':
        break
    else:
        print("Pergjigjia juaj nuk eshte valide!")
        break

UDPClientSocket.close()