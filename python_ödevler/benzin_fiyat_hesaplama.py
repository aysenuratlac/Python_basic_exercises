#problem3:aracın kmde ne kadar yaktığı ve kaç km yol yaptığını alın ve sürücünü toplam ne ödeyeceğini hesaplayın.
km_başı_yakıt=int(input("lütfen aracınızın kilometrede kaç litre yaktığını giriniz:"))
yol=int(input("lütfen aracınızın aldığı yolu km cinsinden giriniz:"))
ihtiyaç=(km_başı_yakıt*yol)
print("aracınızın ihtiyacı olan benzin miktarı:{}".format(ihtiyaç))
#done
Çözümler
Soru 1
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

çarpım = a * b * c

print("{} x {} x {} = {} dir".format(a,b,c,çarpım))
a:1
b:3
c:10
1 x 3 x 10 = 30 dir
Soru 2
boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

print("Beden Kitle İndeksi:",kilo / (boy ** 2))
Boy:1.73
Kilo:84
Beden Kitle İndeksi: 28.06642386982525
Soru 3
yakan_miktar = float(input("Kilometrede yakan miktar:"))

kilometre = int(input("Kaç km yol yaptınız:"))

print("Tutar: {} tl".format(yakan_miktar * kilometre))
Kilometrede yakan miktar:0.22
Kaç km yol yaptınız:430
Tutar: 94.6 tl
Soru 4
ad = input("Ad:")
soyad = input("Soyad:")
numara = input("Numara:")
print("\nBilgiler...\n")
print("{}\n{}\n{}".format(ad,soyad,numara))
Ad:Mustafa Murat
Soyad:Coşkun
Numara:12345
Bilgiler...
Mustafa Murat
Coşkun
12345
Soru 5
a = input("a:")
b = input("b:")
print("Değiştirilmeden Önce Değerler\na: {} b: {}\n".format(a,b))
a,b = b,a
print("Değiştirildikten Sonraki Değerler\na: {} b: {}\n".format(a,b))
a:3
b:4
Değiştirilmeden Önce Değerler
a: 3 b: 4
Değiştirildikten Sonraki Değerler
a: 4 b: 3
Soru 6
a = int(input("a:"))
b = int(input("b:"))
c =  (a ** 2 + b ** 2) ** 0.5
print("Hipotenüs: ",c)
a:3
b:4
Hipotenüs:  5.0