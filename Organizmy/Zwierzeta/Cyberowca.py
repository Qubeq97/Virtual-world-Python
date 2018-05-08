from Organizmy.Zwierze import *


class Cyberowca(Zwierze):
    def __init__(self, x, y, swiat, sila=11, wiek=0):
        Zwierze.__init__(self, x, y, swiat, sila, 4, Gatunek.CYBEROWCA, "Cyberowca", wiek)

    def akcja(self):
        barszczX, barszczY = self._swiat.wspolrzedneBarszczu(self._x,self._y)
        if barszczX is not None and barszczY is not None:
            if barszczX > self._x:
                self._celX = self._x + 1
                self._celY = self._y
            elif barszczX < self._x:
                self._celX = self._x - 1
                self._celY = self._y
            elif barszczY > self._y:
                self._celY = self._y + 1
                self._celX = self._x
            elif barszczY < self._y:
                self._celY = self._y - 1
                self._celX = self._x
            if self._swiat.czyWspolrzedneOk(self._celX, self._celY):
                oponent = self._swiat.zwrocZMapy(self._celX, self._celY)
                if oponent is None:
                    self.poruszSie(self._celX, self._celY)
                elif oponent.getGatunek() == self._gatunek:
                    self.Rozmnoz(oponent)
                elif self.kolizja(oponent):
                    self.poruszSie(self._celX, self._celY)
        else:
            super().akcja()
