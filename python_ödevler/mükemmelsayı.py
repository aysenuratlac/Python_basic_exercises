"""
x=int(input("Lütfen bir sayı giriniz:"))
toplam=0
for i in range(1,x):
    if (x%i==0):
        toplam+=i
if(toplam==x):
    print("Girdiğiniz sayı mükemmel sayıdır.")
else:
    print("Girdiğiniz sayı mükemmel sayı değildir.")
"""
"""a = int(input("Lütfen bir sayı girin:"))
x = 1
toplam = 0
while x < a:
    if a % x == 0:
        toplam += x
        x += 1
if toplam == a:
    print("girdiğiniz sayı mükemel sayıdır.")
else:
    print("girdiğiniz sayı mükemmel DEĞİLDİR!")
"""
for i in range(1,101):
    if i%3==0:
        print(i)


















