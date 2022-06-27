defkullanıcıadı="ayşenur"
defşifre="123"
while True:
    ad= input("kullanıcı adı:")
    şifre= input("şifre:")
    if(defkullanıcıadı!=ad or defşifre!=şifre):
        print("lütfen tekrar deneyin")
    else:
        print("Hoşgeldiniz")
        break
