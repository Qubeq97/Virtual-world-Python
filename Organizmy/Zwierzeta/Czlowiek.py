from Organizmy.Zwierze import *


class Czlowiek(Zwierze):
    def __init__(self, x, y, swiat, sila=5, wiek=0, akt=False, czy=True, tura=0):
        Zwierze.__init__(self, x, y, swiat, sila, 4, Gatunek.CZLOWIEK, "Człowiek", wiek)
        self.__kierunek = 0
        self.__czyAktywna = akt
        self.__czyWolno = czy
        self.__turaSkilla = tura

    def akcja(self, kier=0):
        if kier == 0:  # GÓRA
            self._celX = self._x
            self._celY = self._y - 1
        elif kier == 1:  # DÓŁ
            self._celX = self._x
            self._celY = self._y + 1
        elif kier == 2:  # LEWO
            self._celX = self._x - 1
            self._celY = self._y
        elif kier == 3:  # PRAWO
            self._celX = self._x + 1
            self._celY = self._y
        if self._swiat.czyWspolrzedneOk(self._celX, self._celY):
            oponent = self._swiat.zwrocZMapy(self._celX, self._celY)
            if oponent is None:
                self.poruszSie(self._celX, self._celY)
            elif oponent.getGatunek() == self._gatunek:
                self.Rozmnoz(oponent)
            elif self.kolizja(oponent):
                self.poruszSie(self._celX, self._celY)

        # Działanie samej specjalnej umiejętności:
        if self.__czyAktywna:
            self.__turaSkilla += 1
            self._sila -= 1
            if self.__turaSkilla >= 5:
                self.__czyAktywna = False
                self.__czyWolno = False
                self.__turaSkilla = 0

        # Odliczanie pozostałych tur bana, jeżeli jeszcze nie wolno:
        elif not self.__czyWolno:
            self.__turaSkilla += 1
            if self.__turaSkilla >= 5:
                self.__turaSkilla = 0
                self.__czyWolno = True

    def aktywuj(self):
        # Skill: Magiczny Eliksir (mój indeks 165761, ostatnia cyfra 1, 1 mod 5 == 1)
        if self.__czyWolno and not self.__czyAktywna:
            self._sila += 5
            self.__turaSkilla = 0
            self.__czyAktywna = True


    def czyAktywna(self):
        return self.__czyAktywna

    def czyWolno(self):
        return self.__czyWolno

    def getTura(self):
        return self.__turaSkilla
