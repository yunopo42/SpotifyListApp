import time
from Liste import *

print('''**************
SPOTİFY ŞARKILARIM
Lütfen bir işlem seçin : 
1-)Şarkıları Göster 
2-)Şarkı Bul
3-)Şarkı Ekle
4-)Şarkı Sil
Çıkış Yapmak için Q ya basınız!!!
*************''')

my_list = Listem()

while True:
    islem  = input("Isleminizi girin: ")

    if(islem == '1'):#SHOW MUSİC
        my_list.sarkilari_goster()
    elif(islem == '2'):#FİND MUSİC
        isim = input("Aradığınız şarkı ismini girin : ")
        print("Şarkı aranıyor...")
        time.sleep(2)
        my_list.sarki_ekle(isim)

       
    elif(islem == '3'):#ADD NEW MUSİC
        print("Sırasıyla eklemek istedğiniz yeni şarkıyı girin : ")
        isim = input("ŞARKI ADI : ")
        sarkici = input("Şarkıcı ADI : ")
        tur = input("Şartkı Türü : ")

        yeni_sarki = Sarki(isim,sarkici,tur)
        print("Yeni şarkı ekleniyor...")
        time.sleep(1)
        my_list.sarki_ekle(yeni_sarki)
        print("Şarkı eklendi")
    elif(islem == '4'):#DELETE MUSİC
        my_list.sarkilari_goster()
        isim = input("Hangi şarkıyı silmek istersiniz")
        print("kitap siliniyor...")
        time.sleep(2)
        my_list.sarki_sil(isim)
        print("kitabınız silindi X")

    elif(islem == 'q'):#QUIT APP
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem:404")



