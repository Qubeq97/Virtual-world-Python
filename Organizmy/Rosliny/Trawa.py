from Organizmy.Roslina import *


class Trawa(Roslina):
    def __init__(self, x, y, swiat, wiek=0):
        Roslina.__init__(self, x, y, swiat, 0, Gatunek.TRAWA, "Trawa", wiek)
