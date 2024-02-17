import sqlite3

class Sarki():
    def __init__(self,isim,sarkici,tur):
        self.isim = isim
        self.sarkici = sarkici
        self.tur = tur
    def __str__(self):
        return "ŞARKI : {}\nŞARKICI : {}\nTÜR : {}".format(self.isim,self.sarkici,self.tur)

class Listem():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.con = sqlite3.connect("Listem")
        self.cursor = self.con.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplık(Sarki TEXT,Sarkici TEXT,Tur TEXT)"
        self.cursor.execute(sorgu)
        self.con.commit()
    def baglantiyi_kes(self):
        self.con.close()
    def sarkilari_goster(self):
        sorgu ="SELECT * FROM kitaplık"
        self.cursor.execute(sorgu)
        sarkilar =self.cursor.fetchall()
        if(len(sarkilar)==0):
            print("Kitaplıkda sarki Bulunmuyor")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2])
                print(sarki)
    def sarki_sorgula(self,isim):
        sorgu = "SELECT * From kitaplık WHERE isim = ?"
        self.cursor.execute(sorgu)
        sarki = self.cursor.fetchall()
        if(len(sarki)==0):
            print("Listede Böyle bir sarki YOK!!")
        else:
            for i in sarki:
                sarki = Sarki(i[0][0],i[0][1],i[0][2])
                print(sarki)

    def sarki_ekle(self,sarki):
        sorgu = "INSERT INTO kitaplık VALUES(?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sarkici,sarki.tur))
        self.con.commit()

    def sarki_sil(self,isim):
        sorgu = "DELETE FROM kitaplık WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.con.commit()








