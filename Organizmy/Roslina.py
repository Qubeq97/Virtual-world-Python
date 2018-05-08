from Organizmy.Organizm import *
from Wyjatki import *


class Roslina(Organizm):
    def __init__(self, x, y, swiat, sila, gatunek, nazwa, wiek=0):
        super().__init__(x, y, swiat, sila, 0, gatunek, nazwa, wiek)

    def akcja(self):
        rand = random.randint(0, 1)
        if rand == 0:
            return
        rand = random.randint(0, 3)
        if rand == 0:  # GÓRA
            self._celX = self._x
            self._celY = self._y - 1
        elif rand == 1:  # DÓŁ
            self._celX = self._x
            self._celY = self._y + 1
        elif rand == 2:  # LEWO
            self._celX = self._x - 1
            self._celY = self._y
        elif rand == 3:  # PRAWO
            self._celX = self._x + 1
            self._celY = self._y
        try:
            self._swiat.stworzOrganizm(self._gatunek, self._celX, self._celY)
            return True
        except(FullError, OccupiedError, ValueError):
            return False  # Wartości zwracane tylko na użytek Mlecza

    def obrona(self, atakujacy):
        self.Zabij()
        self._swiat.dopiszDoKonsoli(atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
            atakujacy.getY()) + ")  zjada " + self._nazwa + " (" + str(self._x) + "," + str(self._y) + ")")
        return OdbicieAtaku.WYGRANA
