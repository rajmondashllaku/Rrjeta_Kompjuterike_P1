from socket import *
from datetime import datetime
import random
import os
import string
import math

def IPADDRESS(ClientIpAddr):
    return "IP Adresa e klientit eshte: " + ClientIpAddr

def PORT(ClientPortNo):
    return "Klienti eshte duke perdorur portin: " + str(ClientPortNo)

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

serverName = 'localhost'
serverPort = 13000

UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
UDPServerSocket.bind((serverName, serverPort))

print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort) + '.')

print('Serveri eshte i gatshem te pranoj kerkesa.')

while True:

    bytesAddressPair = UDPServerSocket.recvfrom(1024)

    ClientRequest = bytesAddressPair[0].decode().upper()

    address = bytesAddressPair[1]
    IpAddr = address[0]
    numriPortit = address[1]

    print("Client IP Address:{}".format(address))
    if ClientRequest == "PORT":
        response = PORT(address[1])
    elif ClientRequest == "IPADDRESS":
        response = IPADDRESS(address[0])
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
        response = CONVERT(llojiKonvertimit, vlera)
    elif ClientRequest.startswith("GCF"):
        arg = ClientRequest.split(" ", 2)
        m = float(arg[1])
        n = float(arg[2])
        response = str(GCF(m, n))
    elif ClientRequest.startswith("KATRORI"):
        arg = ClientRequest.split(" ", 1)
        brinja = arg[1]
        response = KATRORI(brinja)
    elif ClientRequest.startswith("CAPITALIZE"):
        arg = ClientRequest.split(" ", 1)
        tekst = arg[1]
        response = CAPITALIZE(tekst)
    else:
        response = "Kerkesa eshte jovalide"

    response = str.encode(response)

    UDPServerSocket.sendto(response, address)
