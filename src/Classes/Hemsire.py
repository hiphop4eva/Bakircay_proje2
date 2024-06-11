from Classes.Personel import *

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman = "", maas = 0, calisma_saati = 0, sertifika = "", hastane = "") -> None:
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def __str__(self) -> str:
        return super().__str__() + f"\nCalisma Saati: {self.__calisma_saati} \nSertifika: {self.__sertifika} \nHastane: {self.__hastane}"

    def maas_arttir(self, rate):
        self._maas += self._maas * (100 + rate)

    def getCalismaSaati(self):
        return self.__calisma_saati

    def getSertifika(self):
        return self.__sertifika

    def getHastane(self):
        return self.__hastane

    def setCalismaSaati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def setSertifika(self, sertifika):
        self.__sertifika = sertifika

    def setHastane(self, hastane):
        self.__hastane = hastane