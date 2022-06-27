"""#Problem1--beden kitle indeksi
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& BEDEN KİTLE İNDEXİ HESAPLAMA PROGRAMI &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

kilo=float(input("lütfen kilonuzu giriniz:"))

boy=float(input("lütfen boyunuzu (metre cinsinde)giriniz:"))
bki=kilo/(boy*boy)
if(bki<18.5):
    print("zayıf")
elif(bki<25):
    print("normal")
elif(bki<=30):
    print("fazla kilolu")
elif(bki):
    print("obez")
"""

""""problem2--3 sayı al en büyüğünü yazdır
print("yapmanız gereken tek şey sırayla 3 sayı girmektir.")
a=float(input("birinci sayı:"))
b=float(input("ikinci sayı:"))
c=float(input("üçüncü sayı:"))

if(a>b):
    if(a>c):
        print("{} en büyük sayıdır.".format(a))
    else:
        print("{} en büyük sayıdır.".format(c))
elif(b>a):
    if(b>c):
        print("{} en büyük sayıdır.".format(b))
    else:
        print("{} en büyük sayıdır.".format(c))  
        """
"""#problem 3--harf notu hsaplama(yüzdelikli)
vize1=float(input("lütfen 1.vize notunuzu girin:"))
vize2=float(input("lütfen 2.vize notunuzu girin:"))
final=float(input("lütfen final notunuzu girin:"))

genel= vize1 *3/10 + vize2 *3/10 +final *4/10
if(genel>=90):
    print("AA")
elif(genel>=85):
    print("BA")
elif (genel >= 80):
    print("BB")
elif (genel>= 75):
    print("CB")
elif (genel >= 70):
    print("CC")
elif (genel >= 65):
    print("DC")
elif (genel >= 60):
    print("DD")
elif (genel >= 55):
    print("FD")
elif(genel<55):
    print("FF")
    """
"""#problem4--şekil hesaplama
şekil=input("tipini bulmak istediğiniz şekli seçiniz(üçgen veya dörtgen):")
if(şekil=="üçgen"):
    x1=float(input("1.kenar uzunluğu:"))
    x2=float(input("2.kenar uzunluğu:"))
    x3=float(input("3.kenar uzunluğu:"))
    if(abs(x1-x3)<x2<x1+x3 and abs(x1-x2)<x3<x1+x2 and abs(x2-x3)<x1<x2+x3 ):
        if(x1==x2==x3):
            print("eşkenar üçgen")
        elif(x1==x2!=x3 or x1==x3!=x2 or x2==x3!=x1):
            print("ikizkenar üçgen")
        else:
             print("çeşitkenar üçgen")
    else:
        print("bir üçgen belirtmez")
if(şekil=="dörtgen"):
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))

    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")"""























