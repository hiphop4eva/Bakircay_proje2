from Classes.Personel import *

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman = "", maas = 0, uzmanlik = "", deneyim_yili = 0, hastane = "") -> None:
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def __str__(self) -> str:
        return super().__str__() + f"\nUzmanlık: {self.__uzmanlik} \nDeneyim Yılı: {self.__deneyim_yili} \nHastane: {self.__hastane}"
    
    def maas_arttir(self, rate):
        self._maas += self._maas * (100 + rate)
    
    def getUzmanlik(self):
        return self.__uzmanlik
    
    def getDeneyimYili(self):
        return self.__deneyim_yili
    
    def getHastane(self):
        return self.__hastane
    
    def setUzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik
    
    def setDeneyimYili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili
    
    def setHastane(self, hastane):
        self.__hastane = hastane