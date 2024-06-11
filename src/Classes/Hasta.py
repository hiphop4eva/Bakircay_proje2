class Hasta():
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi = "", hastalik = "", tedavi = "") -> None:
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def __str__(self) -> str:
        return f"No:{self.__hasta_no} \nAd: {self.__ad} \nSoyad: {self.__soyad} \nDogum Tarihi: {self.__dogum_tarihi} \nHastalık: {self.__hastalik} \nTedavi: {self.__tedavi}"
    
    def tedavi_suresi_hesapla(self):
        tedavi_suresi_ay = 0
        if self.__hastalik == "Grip":
            tedavi_suresi_ay += 1
        elif self.__hastalik == "Enfeksiyon":
            tedavi_suresi_ay += 3
        elif self.__hastalik == "Kanser":
            tedavi_suresi_ay += 12
        else:
            return "Tedavi Suresi Hesaplanamadı."
        
        if self.__tedavi == "Hızlı Tedavi":
            tedavi_suresi_ay += 1
        elif self.__tedavi == "Dengeli Tedavi":
            tedavi_suresi_ay += 3
        elif self.__tedavi == "Dikkatli Tedavi":
            tedavi_suresi_ay += 12
        else:
            return "Tedavi Suresi Hesaplanamadı."
        
        return tedavi_suresi_ay

    def getHastaNo(self):
        return self.__hasta_no
    
    def getAd(self):
        return self.__ad
    
    def getSoyad(self):
        return self.__soyad
    
    def getDogumTarihi(self):
        return self.__dogum_tarihi
    
    def getHastalik(self):
        return self.__hastalik
    
    def getTedavi(self):
        return self.__tedavi
    
    def setHastaNo(self, hasta_no):
        self.__hasta_no = hasta_no
    
    def setAd(self, ad):
        self.__ad = ad
    
    def setSoyad(self, soyad):
        self.__soyad = soyad
    
    def setDogumTarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi