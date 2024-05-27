from Classes.Personel import *

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman = "", maas = 0, uzmanlik = "", deneyim_yili = 0, hastane = "") -> None:
        super().__init__(personel_no, ad, soyad, departman, maas)
        self._uzmanlik = uzmanlik
        self._deneyim_yili = deneyim_yili
        self._hastane = hastane

    def __str__(self) -> str:
        return super().__str__() + f"\nUzmanlık: {self._uzmanlik} \nDeneyim Yılı: {self._deneyim_yili} \nHastane: {self._hastane}"
    
    def maas_arttir(self, rate):
        self._maas += self._maas * (100 + rate)
    
    def getUzmanlik(self):
        return self._uzmanlik
    
    def getDeneyimYili(self):
        return self._deneyim_yili
    
    def getHastane(self):
        return self._hastane
    
    def setUzmanlik(self, uzmanlik):
        self._uzmanlik = uzmanlik
    
    def setDeneyimYili(self, deneyim_yili):
        self._deneyim_yili = deneyim_yili
    
    def setHastane(self, hastane):
        self._hastane = hastane