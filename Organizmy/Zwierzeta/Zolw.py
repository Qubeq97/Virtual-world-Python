from Organizmy.Zwierze import *


class Zolw(Zwierze):
    def __init__(self, x, y, swiat, sila=2, wiek=0):
        super(Zolw, self).__init__(x, y, swiat, sila, 1, Gatunek.ZOLW, "Żółw", wiek)

    def akcja(self):
        rand = random.randint(0, 3)
        if rand == 0:
            super(Zolw, self).akcja()

    def obrona(self, atakujacy):
        if atakujacy.getSila() < 5:
            self._swiat.dopiszDoKonsoli(
                self._nazwa + " (" + str(self._x) + "," + str(
                    self._y) + ")  odpiera atak " + atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
                    atakujacy.getY()) + ")")
            return OdbicieAtaku.WYCOFANIE
        else:
            return super(Zolw, self).obrona(atakujacy)
