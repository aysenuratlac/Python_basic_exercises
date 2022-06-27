#problem4:Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
ad=input("please enter your name:")
soyad=input("please enter your surname:")
numara=input("please enter your number:")
print("{}\n{}\n{}".format(ad,soyad,numara))
#problem5:Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
print("yeni etkinlik sayıların yerlerini değiiştirme")
a=int(input("birinci sayı:"))
b=int(input("ikinci sayı:"))
print("sayıların ilk hali:",a,b)
(a,b)=(b,a)
print("sayıların son hali",a,b)