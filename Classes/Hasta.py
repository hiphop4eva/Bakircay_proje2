class Hasta():
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi = "", hastalik = "", tedavi = "") -> None:
        self._hasta_no = hasta_no
        self._ad = ad
        self._soyad = soyad
        self._dogum_tarihi = dogum_tarihi
        self._hastalik = hastalik
        self._tedavi = tedavi

    def __str__(self) -> str:
        return f"No:{self._hasta_no} \nAd: {self._ad} \nSoyad: {self._soyad} \nDogum Tarihi: {self._dogum_tarihi} \nHastalık: {self._hastalik} \nTedavi: {self._tedavi}"

    def getHastaNo(self):
        return self._hasta_no
    
    def getAd(self):
        return self._ad
    
    def getSoyad(self):
        return self._soyad
    
    def getDogumTarihi(self):
        return self._dogum_tarihi
    
    def getHastalik(self):
        return self._hastalik
    
    def getTedavi(self):
        return self._tedavi
    
    def setHastaNo(self, hasta_no):
        self._hasta_no = hasta_no
    
    def setAd(self, ad):
        self._ad = ad
    
    def setSoyad(self, soyad):
        self._soyad = soyad
    
    def setDogumTarihi(self, dogum_tarihi):
        self._dogum_tarihi = dogum_tarihi