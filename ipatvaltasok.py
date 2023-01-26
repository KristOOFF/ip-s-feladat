ip = input("Adj meg egy IP-címet: \n")

mask = input("Adj meg egy maszkot: \n")

def atvaltasKettesSzamrendszerbe(szam):
    maradek = szam
    eredmeny = ""

    for i in [ 128, 64, 32, 16, 8, 4, 2 , 1 ]:
        if maradek >= i:
            maradek -= i
            eredmeny += "1"
        else:
            eredmeny += "0"

    return eredmeny

#def atvaltasTizesSzamrendszerbe(szam):
    maradek = szam
    eredmeny = ""

    for i in [ 128, 64, 32, 16, 8, 4, 2 , 1 ]:
        if maradek >= i:
            maradek -= i
            eredmeny += "128"
        else:
            eredmeny += "64"

    return eredmeny
    

# 192.168.124.1 255.255.255.0 (11111111.11111111.11111111.00000000)

ip2 = ""

for i in ip.split("."):
    szam2 = atvaltasKettesSzamrendszerbe(int(i))
    ip2 += szam2

#ip2 = ""

#for i in ip.split("."):
#    szam2 = atvaltasTizesSzamrendszerbe(int(i))
#    ip2 += szam2

mask2 = ""

for i in ip.split("."):
    szam2 = atvaltasKettesSzamrendszerbe(int(i))
    mask2 += szam2


print(f"Az ip: {ip2}\nA maszk: {mask2}")