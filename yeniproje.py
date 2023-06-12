import pandas as pd
df = pd.read_excel('veriler.xlsx')
print(df) 

def menu():
    print("Hoşgeldiniz! Umarım iyi bir durumdasınızdır.")
    print("Lütfen bir işlem seçiniz:")
    print("1- Sisteme Üye Ol")
    print("2- Sisteme Giriş Yap")
    print("3- Şifremi Unuttum")
    print("4- Çıkış Yap")
    print("5- Konum bilgilerini güncelle")
    print("6- Hastalık bilgisini güncelle")
    
def menu2():
    print("Lütfen konum seçiniz:")    
    print("1- Veysel Karani Mahallesi")
    print("2- Akpınar Mahallesi")
    print("3- Adil Mahallesi")
    print("4- Eyüp Sultan Mahallesi")
    print("5- Ortadağ Mahallesi")
    

while True:
    menu()
    secim = int(input("İşlem Seçiniz: "))

    if secim == 1:
        print("Sisteme Üye Olma İşlemi")
         ad = input("Adınızı giriniz: ")
        soyad = input("Soyadınızı giriniz: ")
        kullanici_adi = input("Kullanıcı adı belirleyiniz: ")
        sifre = input("Şifre belirleyiniz: ")
        email = input("E-posta adresinizi giriniz: ")

        yeni_kullanici = pd.DataFrame({'Ad': [ad], 'Soyad': [soyad], 'Kullanıcı Adı': [kullanici_adi], 'Şifre': [sifre], 'E-posta': [email]})
        df = df.append(yeni_kullanici, ignore_index=True)
        df.to_excel('veriler.xlsx', index=False)

    elif secim == 2:
        print("Sisteme Giriş Yapma İşlemi")
         print("Sisteme Giriş Yapma İşlemi")
        kullanici_adi = input("Kullanıcı adınızı giriniz: ")
        sifre = input("Şifrenizi giriniz: ")
        if kullanici_adi in df['Kullanıcı Adı'].values and sifre in df['Şifre'].values:
            print("Giriş başarılı.")
        else:
            print("Giriş başarısız. Lütfen tekrar deneyin.")
       
    elif secim == 3:
        print("Şifremi Unuttum İşlemi")
        kullanici_bilgisi = input("Kullanıcı adınızı veya e-posta adresinizi giriniz: ")

        if kullanici_bilgisi in df['Kullanıcı Adı'].values or kullanici_bilgisi in df['E-posta'].values:
            yeni_sifre = "yeni_sifre"  
            sifre_sifirlandi = True  
            print("Şifreniz sıfırlandı. Yeni şifreniz e-posta adresinize gönderildi.")
        else:
            sifre_sifirlandi = False  
            print("Kullanıcı bulunamadı. Lütfen geçerli bir kullanıcı adı veya e-posta adresi girin.")

    elif secim == 4:
        print("Çıkış Yapılıyor...")
        break
        
    elif secim == 5:
        print("Sistemdeki konumu güncelleme işlemi: ")
        menu2()
        secenek = int(input("Konumunuzu seçin: "))
           
        if secenek == 1:
            print("Konumunuz Veysel Karani Mahallesi olarak güncellenmiştir.") 
        elif secenek == 2:
            print("Konumunuz Akpınar Mahallesi olarak güncellenmiştir.")    
        elif secenek == 3:
            print("Konumunuz Adil Mahallesi olarak güncellenmiştir.")
        elif secenek == 4:
            print("Konumunuz Eyüp Sultan Mahallesi olarak güncellenmiştir.")
        elif secenek == 5:
            print("Konumunuz Ortadağ Mahallesi olarak güncellenmiştir.")  
           
    elif secim == 6:
        print("Sistemdeki hastalık bilgisi güncelleme işlemi")
        kullanici_adi = input("Kullanıcı adınızı giriniz: ")
    
       if kullanici_adi in df['Kullanıcı Adı'].values:
        hastalik = input("Güncel hastalık bilgisini giriniz: ")
        df.loc[df['Kullanıcı Adı'] == kullanici_adi, 'Hastalık'] = hastalik
        df.to_excel('veriler.xlsx', index=False)
        print("Hastalık bilgisi güncellendi.")
       else:
        print("Kullanıcı bulunamadı. Lütfen geçerli bir kullanıcı adı girin.")

    else:
        print("Geçersiz işlem seçimi! Lütfen tekrar deneyin.")


