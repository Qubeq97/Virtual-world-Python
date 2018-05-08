from Organizmy.Roslina import *


class Mlecz(Roslina):
    def __init__(self, x, y, swiat, wiek=0):
        Roslina.__init__(self, x, y, swiat, 0, Gatunek.MLECZ, "Mlecz", wiek)

    def akcja(self):
        for i in range(0, 3):
            if super().akcja():
                break
