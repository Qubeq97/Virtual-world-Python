from Organizmy.Roslina import *


class Jagody(Roslina):
    def __init__(self, x, y, swiat, wiek=0):
        Roslina.__init__(self, x, y, swiat, 10, Gatunek.JAGODY, "Wilcze Jagody", wiek)

    def obrona(self, atakujacy):
        self.Zabij()
        self._swiat.dopiszDoKonsoli(atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
            atakujacy.getY()) + ")  zjada " + self._nazwa + " (" + str(self._x) + "," + str(self._y) + ") i ginie")
        return OdbicieAtaku.PRZEGRANA
