from Organizmy.Zwierze import *


class Owca(Zwierze):
    def __init__(self, x, y, swiat, sila=4, wiek=0):
        Zwierze.__init__(self, x, y, swiat, sila, 4, Gatunek.OWCA, "Owca", wiek)
