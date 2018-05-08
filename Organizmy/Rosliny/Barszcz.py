from Organizmy.Roslina import *
from Organizmy.Zwierze import Zwierze


class Barszcz(Roslina):
    def __init__(self, x, y, swiat, wiek=0):
        Roslina.__init__(self, x, y, swiat, 99, Gatunek.BARSZCZ, "Barszcz Sosnowskiego", wiek)

    def obrona(self, atakujacy):
        self.Zabij()
        if atakujacy.getGatunek() != Gatunek.CYBEROWCA:
            self._swiat.dopiszDoKonsoli(atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
                atakujacy.getY()) + ")  zjada " + self._nazwa + " (" + str(self._x) + "," + str(self._y) + ") i ginie")
            return OdbicieAtaku.PRZEGRANA
        else:
            self._swiat.dopiszDoKonsoli(atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
                atakujacy.getY()) + ")  zjada " + self._nazwa + " (" + str(self._x) + "," + str(self._y) + ")")
            return OdbicieAtaku.WYGRANA

    def akcja(self):
        for i in range(0, 3):
            if i == 0:  # GÓRA
                self._celX = self._x
                self._celY = self._y - 1
            elif i == 1:  # DÓŁ
                self._celX = self._x
                self._celY = self._y + 1
            elif i == 2:  # LEWO
                self._celX = self._x - 1
                self._celY = self._y
            elif i == 3:  # PRAWO
                self._celX = self._x + 1
                self._celY = self._y
            if self._swiat.czyWspolrzedneOk(self._celX, self._celY):
                test = self._swiat.zwrocZMapy(self._celX, self._celY)
                if test is not None:
                    if isinstance(test, Zwierze):
                        if test.getGatunek() != Gatunek.CYBEROWCA:
                            test.Zabij()
                            self._swiat.dopiszDoKonsoli(
                                self._nazwa + " (" + str(self._x) + "," + str(
                                    self._y) + ")  zabija " + test.getNazwa() + " (" + str(
                                    test.getX()) + "," + str(
                                    test.getY()) + ")")
                        else:
                            self._swiat.dopiszDoKonsoli(
                                self._nazwa + " (" + str(self._x) + "," + str(
                                    self._y) + ")  nie daje rady z: " + test.getNazwa() + " (" + str(
                                    test.getX()) + "," + str(
                                    test.getY()) + ")")
        super().akcja()
