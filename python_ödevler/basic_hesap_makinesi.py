print("""**********************************
Basit Hesap Makinesi Programı

İşlemler
1=toplama işlemi

2.çıkarma işlemi

3.çarpma işlemi

4.bölme işlemi

***********************************""")
a=float(input("birinci sayı:"))
b=float(input("ikinci sayı:"))
işlem=float(input("işleminizi girin:"))
if(işlem==1):
    print("{} ve {} nin toplamı {} dir".format(a,b,a+b))
if(işlem==2):
    print("{} ve {} nin farkı {} dir".format(a,b,a-b))
if (işlem == 3):
    print("{} ve {} nin çarpımı {} dir".format(a, b, a*b))
if(işlem==4):
    print("{} ve {} nin bölümü {} dir".format(a,b,a/b))
else:
    print("Geçersiz işlem...")