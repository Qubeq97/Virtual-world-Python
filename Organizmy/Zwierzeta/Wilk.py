from Organizmy.Zwierze import *


class Wilk(Zwierze):
    def __init__(self, x, y, swiat, sila=9, wiek=0):
        Zwierze.__init__(self, x, y, swiat, sila, 5, Gatunek.WILK, "Wilk", wiek)
