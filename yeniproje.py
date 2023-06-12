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

    elif secim == 2:
        print("Sisteme Giriş Yapma İşlemi")
       
    elif secim == 3:
        print("Şifremi Unuttum İşlemi")

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
        
    else:
        print("Geçersiz işlem seçimi! Lütfen tekrar deneyin.")


