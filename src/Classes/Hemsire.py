from Classes.Personel import *

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman = "", maas = 0, calisma_saati = 0, sertifika = "", hastane = "") -> None:
        super().__init__(personel_no, ad, soyad, departman, maas)
        self._calisma_saati = calisma_saati
        self._sertifika = sertifika
        self._hastane = hastane

    def __str__(self) -> str:
        return super().__str__() + f"\nCalisma Saati: {self._calisma_saati} \nSertifika: {self._sertifika} \nHastane: {self._hastane}"

    def maas_arttir(self, rate):
        self._maas += self._maas * (100 + rate)

    def getCalismaSaati(self):
        return self._calisma_saati

    def getSertifika(self):
        return self._sertifika

    def getHastane(self):
        return self._hastane

    def setCalismaSaati(self, calisma_saati):
        self._calisma_saati = calisma_saati

    def setSertifika(self, sertifika):
        self._sertifika = sertifika

    def setHastane(self, hastane):
        self._hastane = hastane