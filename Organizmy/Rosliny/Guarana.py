from Organizmy.Roslina import *


class Guarana(Roslina):
    def __init__(self, x, y, swiat, wiek=0):
        Roslina.__init__(self, x, y, swiat, 0, Gatunek.GUARANA, "Guarana", wiek)

    def obrona(self, atakujacy):
        self.Zabij()
        atakujacy.dodajSile(3)
        self._swiat.dopiszDoKonsoli(atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
            atakujacy.getY()) + ")  zjada " + self._nazwa + " (" + str(self._x) + "," + str(self._y) + ") i dostaje + 3 do siły")
        return OdbicieAtaku.WYGRANA
