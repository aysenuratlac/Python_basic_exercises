# problem1:kullanıcıdan 3 sayı al ve çarpımlarını format() metoduyla yazdır.---done
sayı1=int(input("lütfen bir sayı giriniz:"))
sayı2=int(input("lütfen bir sayı daha giriniz:"))
sayı3=int(input("lütfen son bir sayı daha giriniz:"))
çarpımları=(sayı1*sayı2*sayı3)
print("cevabınız: {}".format(çarpımları))

#problem6:dik üçgenin dik iki kenarını(a,b) alın ve hipotenüsü bulmaya çalışın.(Hipotenüs:a^2+b^2 =c^2)--done
a=int(input("birinci dik kenar:"))
b=int(input("ikinci dik kenar:"))
hipo=(a**2+b**2)**(1/2)
print("hipotenüs uzunluğu:",hipo)