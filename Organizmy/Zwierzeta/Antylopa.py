from Organizmy.Zwierze import *



class Antylopa(Zwierze):
    def __init__(self, x, y, swiat, sila=4, wiek=0):
        Zwierze.__init__(self, x, y, swiat, sila, 4, Gatunek.ANTYLOPA, "Antylopa", wiek)

    def akcja(self):
        rand = random.randint(0, 3)
        if rand == 0:  # GÓRA
            self._celX = self._x
            self._celY = self._y - 2
        elif rand == 1:  # DÓŁ
            self._celX = self._x
            self._celY = self._y + 2
        elif rand == 2:  # LEWO
            self._celX = self._x - 2
            self._celY = self._y
        elif rand == 3:  # PRAWO
            self._celX = self._x + 2
            self._celY = self._y
        if self._swiat.czyWspolrzedneOk(self._celX, self._celY):
            oponent = self._swiat.zwrocZMapy(self._celX, self._celY)
            if oponent is None:
                self.poruszSie(self._celX, self._celY)
            elif oponent.getGatunek() == self._gatunek:  # implementuj roznmażanie
                self.Rozmnoz(oponent)
            elif self.kolizja(oponent):
                self.poruszSie(self._celX, self._celY)

    def znajdzWolne(self):
        starycelX, starycelY = self._celX, self._celY
        proba = 0
        while proba <= 3:
            if proba == 0:
                self._celX = self._x
                self._celY = self._y - 1
            elif proba == 1:
                self._celX = self._x
                self._celY = self._y + 1
            elif proba == 2:
                self._celX = self._x - 1
                self._celY = self._y
            elif proba == 3:
                self._celX = self._x + 1
                self._celY = self._y
            if self._swiat.czyWspolrzedneOk(self._celX, self._celY) and  self._swiat.zwrocZMapy(self._celX, self._celY) is None:
                    return True
            else:
                proba += 1
        self._celX = starycelX
        self._celY = starycelY
        return False

    def kolizja(self, oponent):
        rand = random.randint(0, 1)
        if rand == 0:
            return Zwierze.kolizja(self, oponent)
        elif self.znajdzWolne():
            return True
        else:
            return Zwierze.kolizja(self, oponent)

    def obrona(self, atakujacy):
        rand = random.randint(0, 1)
        if rand == 0:
            return Zwierze.obrona(self, atakujacy)
        elif self.znajdzWolne():
            self.poruszSie(self._celX, self._celY)
            self._swiat.dopiszDoKonsoli(
                self._nazwa + " (" + str(self._x) + "," + str(
                    self._y) + ")  ucieka przed " + atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
                    atakujacy.getY()) + ")")
            return OdbicieAtaku.WOLNEPOLE
        else:
            return Zwierze.obrona(self, atakujacy)
