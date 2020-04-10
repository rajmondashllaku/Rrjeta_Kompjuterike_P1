import string
from socket import *
import random
from datetime import datetime
import sys
import os
from threading import *
from _thread import *
import math


# ipaddress
def IPADDRESS(IPAddr):
    return "IP adresa e klientit eshte " + IPAddr

# porti
def PORT(numriPortit):
    return "Klienti eshte duke perdorur portin " + str(numriPortit)

  # count
def COUNT(tekst):
    type(tekst)
    vowels = 0
    consonants = 0
    others = 0

    for i in tekst:
        if (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Y'
                or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y'
        ):

            vowels = vowels + 1
        elif i not in string.ascii_letters:

            others = others + 1
        else:
            consonants = consonants + 1

    return "Teksti i pranuar permban " + str(consonants) + " bashkentingellore dhe " + str(vowels) + " zanore."


# palindrome
def PALINDROME(shkrim):
    if shkrim == shkrim[::-1]:
        return "Teksi eshte palindrom"
    else:
        return "Teksi nuk eshte palindrom"


# game
def GAME():
    resp = ""
    for x in range(5):
        resp = resp + str(random.randint(1, 35))
        if x < 6:
            resp = resp + ", "
    return resp


 # time
def TIME():
   return str(datetime.now())
# reverse
def REVERSE(texti):
    reversed = texti[::-1]
    return "Teksi reversed eshte "+reversed
# gfc
def GCF(a, b):
        if a % b == 0:
            return b
        return GCF(b, a % b)
#convert
def CONVERT(llojiKonvertimit, vlera):
    if llojiKonvertimit.upper() == "CmToFeet".upper():
        cm = vlera
        feet = round(float(cm) / 30.48, 2)
        return str(cm) + " cm = " + str(feet) + " feet"
    elif llojiKonvertimit.upper() == "FeetToCm".upper():
        feet = vlera
        cm = round(float(feet) * 30.48, 2)
        return str(feet) + " feet = " + str(cm) + " cm"
    elif llojiKonvertimit.upper() == "KmToMiles".upper():
        km = vlera
        miles = round(float(km) / 1.609, 2)
        return str(km) + " km = " + str(miles) + " miles"
    elif llojiKonvertimit.upper() == "MilesToKm".upper():
        miles = vlera
        km = round(float(miles) * 1.609, 2)
        return str(miles) + " miles = " + str(km) + " km"
    else:
        return "Nuk ekziston kjo kerkese"

#katrori
def KATRORI(brinja):
    type(brinja)
    syprina=pow(float(brinja),2)
    perimetri=round(4*float(brinja),2)
    return "siperfaqja eshte " + str(syprina) + "dhe perimetri eshte " + str(perimetri)+"."
#capitalize
def CAPITALIZE(tekst):
    type(tekst)
    return tekst.lower().capitalize()
# threaded
def tr(c, addr):
    while True:

        ClientRequest = c.recv(1024).decode()
        if not ClientRequest:
            print('No client request')
            break

        ClientRequest = ClientRequest.upper()

        if ClientRequest == "PORT":
            response = PORT(addr[1])
        elif ClientRequest == "IPADDRESS":
            response = IPADDRESS(addr[0])
        elif ClientRequest.startswith("COUNT"):
            arg = ClientRequest.split(" ", 1)
            tekst = arg[1]
            response = COUNT(tekst)
        elif ClientRequest.startswith("REVERSE"):
            arg = ClientRequest.split(" ", 1)
            texti = arg[1]
            response = REVERSE(texti)
        elif ClientRequest == "TIME":
            response = TIME()
        elif ClientRequest == "GAME":
            response = GAME()
        elif ClientRequest.startswith("PALINDROME"):
            arg = ClientRequest.split(" ", 1)
            shkrim = arg[1]
            response = PALINDROME(shkrim)
        elif ClientRequest.startswith("CONVERT"):
            args = ClientRequest.split(" ", 2)
            llojiKonvertimit = args[1]
            vlera = int(args[2])
            response = CONVERT(llojiKonvertimit,vlera)
        elif ClientRequest.startswith("GCF"):
            arg = ClientRequest.split(" ",2)
            m = float(arg[1])
            n = float(arg[2])
            response = str(GCF(m, n))
        elif ClientRequest.startswith("KATRORI"):
            arg=ClientRequest.split(" ",1)
            brinja=arg[1]
            response = KATRORI(brinja)
        elif ClientRequest.startswith("CAPITALIZE"):
            arg=ClientRequest.split(" ",1)
            tekst=arg[1]
            response=CAPITALIZE(tekst)
        else:
            response = "Kerkesa eshte jovalide"
        c.send(response.encode())
    c.close()


def Main():
    serverName = 'localhost'
    serverPort = 13000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort) + '.')
    serverSocket.listen(5)
    print('Serveri eshte i gatshem te pranoj kerkesa.')
    while True:
        connectionSocket, addr = serverSocket.accept()
        IpAdresaKlientit = addr[0]
        NumriPortitKlientit = addr[1]
        print('Klienti u lidh ne serverin ' + IpAdresaKlientit + ' me portin ' + str(NumriPortitKlientit))
        start_new_thread(tr, (connectionSocket, addr,))
    serverSocket.close()

    connectionSocket.send(response.encode())


if __name__ == '__main__':
    Main()
