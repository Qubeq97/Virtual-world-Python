from Organizmy.Organizm import *
from Wyjatki import *


class Zwierze(Organizm):
    def __init__(self, x, y, swiat, sila, inicjatywa, gatunek, nazwa, wiek=0):
        super().__init__(x, y, swiat, sila, inicjatywa, gatunek, nazwa, wiek)

    def poruszSie(self, celX, celY):
        self._swiat.updatujMape(self, celX, celY)
        self._x = celX
        self._y = celY

    def akcja(self):
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
        if self._swiat.czyWspolrzedneOk(self._celX, self._celY):
            oponent = self._swiat.zwrocZMapy(self._celX, self._celY)
            if oponent is None:
                self.poruszSie(self._celX, self._celY)
            elif oponent.getGatunek() == self._gatunek:  # implementuj roznmażanie
                self.Rozmnoz(oponent)
            elif self.kolizja(oponent):
                self.poruszSie(self._celX, self._celY)

    def Rozmnoz(self, partner):
        kierunek = random.randint(0, 3)
        tryb = random.randint(0, 1)  # 0 - obok siebie, 1 - obok partnera
        licznikProb = 0
        koniec = False
        while not koniec:
            if kierunek == 0:  # GÓRA
                if tryb == 0:
                    self._celX = self._x
                    self._celY = self._y - 1
                else:
                    self._celX = partner.getX()
                    self._celY = partner.getY() - 1
            elif kierunek == 1:  # DÓŁ
                if tryb == 0:
                    self._celX = self._x
                    self._celY = self._y + 1
                else:
                    self._celX = partner.getX()
                    self._celY = partner.getY() + 1
            elif kierunek == 2:  # LEWO
                if tryb == 0:
                    self._celX = self._x - 1
                    self._celY = self._y
                else:
                    self._celX = partner.getX() - 1
                    self._celY = partner.getY()
            elif kierunek == 3:  # PRAWO
                if tryb == 0:
                    self._celX = self._x + 1
                    self._celY = self._y
                else:
                    self._celX = partner.getX() + 1
                    self._celY = partner.getY()
            try:
                self._swiat.stworzOrganizm(self._gatunek, self._celX, self._celY)
                self._swiat.dopiszDoKonsoli(
                    "Nowe zwierze: " + self._nazwa + " (" + str(self._celX) + "," + str(self._celY)+")")
            except FullError:
                break
            except (ValueError, OccupiedError):
                licznikProb += 1
                if licznikProb >= 8:
                    break
                if tryb == 1:
                    kierunek += 1
                    kierunek %= 4
                tryb += 1
                tryb %= 2

    def kolizja(self, oponent):  # true oznacza zgodę na ruch organizmu
        wynik = oponent.obrona(self)
        if wynik == OdbicieAtaku.WYGRANA or wynik == OdbicieAtaku.WOLNEPOLE:
            return True
        elif wynik == OdbicieAtaku.PRZEGRANA:
            self.Zabij()
        return False

    def obrona(self, atakujacy):
        if self._sila <= atakujacy.getSila():
            self.Zabij()
            self._swiat.dopiszDoKonsoli(atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
                atakujacy.getY()) + ")  wygrywa z " + self._nazwa + " (" + str(self._x) + "," + str(self._y) + ")")
            return OdbicieAtaku.WYGRANA
        else:
            self._swiat.dopiszDoKonsoli(
                self._nazwa + " (" + str(self._x) + "," + str(
                    self._y) + ")  wygrywa z " + atakujacy.getNazwa() + " (" + str(atakujacy.getX()) + "," + str(
                    atakujacy.getY()) + ")")
            return OdbicieAtaku.PRZEGRANA
