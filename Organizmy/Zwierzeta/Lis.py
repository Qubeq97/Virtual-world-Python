from Organizmy.Zwierze import *


class Lis(Zwierze):
    def __init__(self, x, y, swiat, sila=3, wiek=0):
        Zwierze.__init__(self, x, y, swiat, sila, 7, Gatunek.LIS, "Lis", wiek)

    def kolizja(self, oponent):  # true oznacza zgodę na ruch organizmu
        if oponent.getSila() > self._sila:
            return False  # Brak zgody na ruch Lisa
        else:
            return Zwierze.kolizja(self, oponent)