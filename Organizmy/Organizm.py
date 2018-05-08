from enum import Enum
from functools import total_ordering
import random
from Swiat import *


class Gatunek(Enum):
    WILK = 1
    OWCA = 2
    LIS = 3
    ZOLW = 4
    ANTYLOPA = 5
    TRAWA = 6
    MLECZ = 7
    GUARANA = 8
    JAGODY = 9
    BARSZCZ = 10
    CZLOWIEK = 11
    CYBEROWCA = 12


class OdbicieAtaku(Enum):
    WYGRANA, WYCOFANIE, PRZEGRANA, WOLNEPOLE = range(4)


@total_ordering
class Organizm:
    def __init__(self, x, y, swiat, sila, inicjatywa, gatunek, nazwa, wiek=0):
        self._x = x
        self._y = y
        self._celX = x
        self._celY = y
        self._swiat = swiat
        self._inicjatywa = inicjatywa
        self._sila = sila
        self._gatunek = gatunek
        self._zywy = True
        self._wiek = wiek
        self._nazwa = nazwa

    # WIRTUALNA!
    def akcja(self):
        pass

    # WIRTUALNA!
    def obrona(self, atakujacy):
        pass

    def postarz(self):
        self._wiek += 1

    def dodajSile(self, ile):
        self._sila += ile

    def Zabij(self):
        self._zywy = False
        self._swiat.usunZMapy(self)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getGatunek(self):
        return self._gatunek

    def getSila(self):
        return self._sila

    def getInicjatywa(self):
        return self._inicjatywa

    def czyZywy(self):
        return self._zywy

    def getNazwa(self):
        return self._nazwa

    def getWiek(self):
        return self._wiek

    def __eq__(self, other):
        return self._inicjatywa == other.getInicjatywa() and self.wiek == other.getWiek()

    def __lt__(self, other):
        if self._inicjatywa == other.getInicjatywa():
            return self._wiek < other.getWiek()
        else:
            return self._inicjatywa < other.getInicjatywa()
