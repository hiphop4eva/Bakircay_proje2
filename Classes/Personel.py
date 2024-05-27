class Personel:
    def __init__(self, personel_no, ad, soyad, departman = "", maas = 0) -> None:
        self._personel_no = personel_no
        self._ad = ad
        self._soyad = soyad
        self._departman = departman
        self._maas = maas

    def __str__(self) -> str:
        return f"No:{self._personel_no} \nAd: {self._ad} \nSoyad: {self._soyad} \nDepartman: {self._departman} \nMaas: {self._maas}",

    def getPersonelNo(self):
        return self._personel_no
    
    def getAd(self):
        return self._ad
    
    def getSoyad(self):
        return self._soyad
    
    def getDepartman(self):
        return self._departman
    
    def getMaas(self):
        return self._maas
    
    def setPersonelNo(self, personel_no):
        self._personel_no = personel_no
    
    def setAd(self, ad):
        self._ad = ad
    
    def setSoyad(self, soyad):
        self._soyad = soyad
    
    def setDepartman(self, departman):
        self._departman = departman
    
    def setMaas(self, maas):
        self._maas = maas