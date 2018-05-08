from Organizmy.Rosliny.Mlecz import Mlecz
from Organizmy.Rosliny.Jagody import Jagody
from Organizmy.Rosliny.Guarana import Guarana
from Organizmy.Rosliny.Trawa import Trawa
from Organizmy.Rosliny.Barszcz import Barszcz
from Organizmy.Zwierzeta.Antylopa import Antylopa
from Organizmy.Zwierzeta.Czlowiek import Czlowiek
from Organizmy.Zwierzeta.Cyberowca import Cyberowca
from Organizmy.Zwierzeta.Lis import Lis
from Organizmy.Zwierzeta.Owca import Owca
from Organizmy.Zwierzeta.Wilk import Wilk
from Organizmy.Zwierzeta.Zolw import Zolw
from Organizmy.Organizm import *
from Organizmy.Roslina import *
from Organizmy.Zwierze import *
from Wyjatki import *
from przycisk import *
import random
import pygame
import ctypes


class Swiat:
    # W poniższych src oznacza nazwę pliku.
    def __init__(self, src=None, x=20, y=20):
        if src is not None:
            self.wczytaj(src)
        else:
            if x * y <= 25:
                raise ValueError
            self.__x = x
            self.__y = y
            self.__liczbaOrganizmow = 0
            self.__maxOrganizmow = x * y
            self.__gdzieCzlowiek = None
            self.__ileBarszczy = False
            self.__organizmy = list()
            self.__nowa = list()
            self.__konsola = list()
            self.__mapa = [[None for j in range(y)] for i in range(x)]
            self.startuj()
        self.__wymiar = 20
        self.__przycisk1 = Przycisk("Wczytaj", self.__x * self.__wymiar + 10, 6 * 15)
        self.__przycisk2 = Przycisk("Zapisz", self.__x * self.__wymiar + 10, 9 * 15)
        self.__przycisk3 = Przycisk("ELIKSIR", self.__x * self.__wymiar + 10, 12 * 15)
        self.__przycisk4 = Przycisk("NOWA TURA", self.__x * self.__wymiar + 10, 15 * 15)

    def zapisz(self, src):
        """
        FORMAT ZAPISU:
        --- ze świata: ---
        x
        y
        ile organizmow
        --- z organizmu: ---
        gatunek
        getX
        getY
        sila
        wiek
        (aktywna)
        (wolno)
        (tura)
        """
        try:
            plik = open(src, 'w')
            plik.write(str(self.__x) + '\n')
            plik.write(str(self.__y) + '\n')
            plik.write(str(self.__liczbaOrganizmow) + '\n')
            for org in self.__organizmy:
                if org is not None and org.czyZywy():
                    plik.write(str(org.getGatunek().value) + '\n')
                    plik.write(str(org.getX()) + '\n')
                    plik.write(str(org.getY()) + '\n')
                    plik.write(str(org.getSila()) + '\n')
                    plik.write(str(org.getWiek()) + '\n')
                    if org.getGatunek() == Gatunek.CZLOWIEK:
                        plik.write(str(int(org.czyAktywna())) + '\n')
                        plik.write(str(int(org.czyWolno())) + '\n')
                        plik.write(str(org.getTura()) + '\n')
        except Exception as e:
            raise e
        finally:
            plik.close()

            """
            FORMAT ZAPISU:
            --- ze świata: ---
            x
            y
            ile organizmow
            --- z organizmu: ---
            gatunek
            getX
            getY
            sila
            wiek
            (aktywna)
            (wolno)
            (tura) - te w nawiasach dotyczą tylko CZŁOWIEKA
            """

    def wczytaj(self, src):
        self.__gdzieCzlowiek = None
        self.__ileBarszczy = 0
        try:
            plik = open(src, 'r')
            x = int(plik.readline())
            y = int(plik.readline())
            if x * y <= 25:
                raise ValueError
            self.__x = x
            self.__y = y
            self.__mapa = [[None for j in range(self.__y)] for i in range(self.__x)]
            self.__maxOrganizmow = self.__x * self.__y
            self.__liczbaOrganizmow = int(plik.readline())
            self.__organizmy = list()
            self.__nowa = list()
            self.__konsola = list()
            if self.__liczbaOrganizmow > self.__maxOrganizmow:
                raise ValueError
            for i in range(0, self.__liczbaOrganizmow):
                nowy_gatunek = Gatunek(int(plik.readline()))
                nowy_x = int(plik.readline())
                nowy_y = int(plik.readline())
                nowy_sila = int(plik.readline())
                nowy_wiek = int(plik.readline())
                if nowy_gatunek == Gatunek.CZLOWIEK:
                    nowy_aktywna = bool(int(plik.readline()))
                    nowy_wolno = bool(int(plik.readline()))
                    nowy_tura = int(plik.readline())
                    if self.__gdzieCzlowiek is None:
                        nowy = Czlowiek(nowy_x, nowy_y, self, nowy_sila, nowy_wiek, nowy_aktywna, nowy_wolno, nowy_tura)
                        self.__gdzieCzlowiek = nowy
                    else:
                        raise ValueError
                else:
                    if nowy_gatunek == Gatunek.ANTYLOPA:
                        nowy = Antylopa(nowy_x, nowy_y, self, nowy_sila, nowy_wiek)
                    elif nowy_gatunek == Gatunek.BARSZCZ:
                        nowy = Barszcz(nowy_x, nowy_y, self, nowy_wiek)
                        self.__ileBarszczy += 1
                    elif nowy_gatunek == Gatunek.CYBEROWCA:
                        nowy = Cyberowca(nowy_x, nowy_y, self, nowy_sila, nowy_wiek)
                    elif nowy_gatunek == Gatunek.LIS:
                        nowy = Lis(nowy_x, nowy_y, self, nowy_sila, nowy_wiek)
                    elif nowy_gatunek == Gatunek.WILK:
                        nowy = Wilk(nowy_x, nowy_y, self, nowy_sila, nowy_wiek)
                    elif nowy_gatunek == Gatunek.OWCA:
                        nowy = Owca(nowy_x, nowy_y, self, nowy_sila, nowy_wiek)
                    elif nowy_gatunek == Gatunek.ZOLW:
                        nowy = Zolw(nowy_x, nowy_y, self, nowy_sila, nowy_wiek)
                    elif nowy_gatunek == Gatunek.GUARANA:
                        nowy = Guarana(nowy_x, nowy_y, self, nowy_wiek)
                    elif nowy_gatunek == Gatunek.MLECZ:
                        nowy = Mlecz(nowy_x, nowy_y, self, nowy_wiek)
                    elif nowy_gatunek == Gatunek.TRAWA:
                        nowy = Trawa(nowy_x, nowy_y, self, nowy_wiek)
                    elif nowy_gatunek == Gatunek.JAGODY:
                        nowy = Jagody(nowy_x, nowy_y, self, nowy_wiek)
                self.__mapa[nowy_x][nowy_y] = nowy
                self.__organizmy.append(nowy)
        except Exception as e:
            raise e
        finally:
            plik.close()

    def setScreen(self, screen):
        self.__screen = screen

    def poruszCzlowieka(self):
        font = pygame.font.Font(None, 18)
        # Teksty po prawej stronie ekranu
        self.__screen.fill((0, 0, 0))
        text = font.render("Twoja kolej!", True,
                           (255, 255, 255))
        self.__screen.blit(text, (
            self.__x * self.__wymiar, 0))
        for x in range(0, self.__x):
            for y in range(0, self.__y):
                org = self.__mapa[x][y]
                if org is not None:
                    if isinstance(org, Czlowiek):
                        color = (255, 0, 0)
                        symbol = '$'
                    else:
                        nazwa = org.getNazwa()
                        if isinstance(org, Lis):
                            color = (237, 75, 0)
                        elif isinstance(org, Antylopa):
                            color = (127, 140, 74)
                        elif isinstance(org, Cyberowca):
                            color = (6, 115, 135)
                        elif isinstance(org, Owca):
                            color = (5, 135, 25)
                        elif isinstance(org, Wilk):
                            color = (0, 0, 0)
                        elif isinstance(org, Zolw):
                            color = (63, 119, 84)
                        elif isinstance(org, Jagody):
                            color = (122, 52, 124)
                        elif isinstance(org, Barszcz):
                            color = (124, 51, 51)
                        elif isinstance(org, Mlecz):
                            color = (151, 158, 33)
                        elif isinstance(org, Guarana):
                            color = (216, 93, 0)
                        elif isinstance(org, Trawa):
                            color = (0, 255, 0)
                        if isinstance(org, Jagody):
                            symbol = "Ja"
                        else:
                            symbol = nazwa[0:2]
                else:
                    color = (170, 170, 170)
                    symbol = ' '
                pygame.draw.rect(self.__screen, color,
                                 pygame.Rect(x * self.__wymiar, y * self.__wymiar, self.__wymiar, self.__wymiar))
                text = font.render(symbol, True, (255, 255, 255))
                self.__screen.blit(text, (
                    x * self.__wymiar - text.get_width() // 2 + self.__wymiar / 2,
                    y * self.__wymiar - text.get_height() // 2 + self.__wymiar / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        return 0
                    elif event.key == pygame.K_DOWN:
                        return 1
                    elif event.key == pygame.K_LEFT:
                        return 2
                    elif event.key == pygame.K_RIGHT:
                        return 3
                elif event.type == pygame.QUIT:
                    exit(0)

    def pokazKomunikat(self, slowo):
        ctypes.windll.user32.MessageBoxW(0, slowo, "Wirtualny świat", 0)

    def dopiszDoKonsoli(self, napis):
        self.__konsola.insert(0, napis)

    def parseBool(self, bool):
        if not bool:
            return "NIE"
        else:
            return "TAK"

    def renderuj(self):
        font = pygame.font.Font(None, 18)

        # Teksty po prawej stronie ekranu
        self.__screen.fill((0, 0, 0))
        text = font.render("Wirtualny świat", True,
                           (255, 255, 255))
        self.__screen.blit(text, (
            self.__x * self.__wymiar, 0))
        if self.__gdzieCzlowiek is not None:
            text = font.render("Specskill aktywny: " + self.parseBool(self.__gdzieCzlowiek.czyAktywna()), True,
                               (255, 255, 255))
            self.__screen.blit(text, (
                self.__x * self.__wymiar, 2 * 15))
            text = font.render("Czy wolno: " + self.parseBool(self.__gdzieCzlowiek.czyWolno()), True, (255, 255, 255))
            self.__screen.blit(text, (
                self.__x * self.__wymiar, 3 * 15))
            text = font.render("Tura działania: " + str(self.__gdzieCzlowiek.getTura()), True, (255, 255, 255))
            self.__screen.blit(text, (
                self.__x * self.__wymiar, 4 * 15))
            text = font.render("Siła człowieka: " + str(self.__gdzieCzlowiek.getSila()), True, (255, 255, 255))
            self.__screen.blit(text, (
                self.__x * self.__wymiar, 5 * 15))
        else:
            text = font.render("Brak człowieka", True,
                               (255, 255, 255))
            self.__screen.blit(text, (
                self.__x * self.__wymiar, 2 * 15))

        # Renderowanie przycisków
        self.__przycisk1.render(self.__screen)
        self.__przycisk2.render(self.__screen)
        self.__przycisk3.render(self.__screen)
        self.__przycisk4.render(self.__screen)

        # Rysowanie mapy
        for x in range(0, self.__x):
            for y in range(0, self.__y):
                org = self.__mapa[x][y]
                if org is not None:
                    if isinstance(org, Czlowiek):
                        color = (255, 0, 0)
                        symbol = '$'
                    else:
                        nazwa = org.getNazwa()
                        if isinstance(org, Lis):
                            color = (237, 75, 0)
                        elif isinstance(org, Antylopa):
                            color = (127, 140, 74)
                        elif isinstance(org, Cyberowca):
                            color = (6, 115, 135)
                        elif isinstance(org, Owca):
                            color = (5, 135, 25)
                        elif isinstance(org, Wilk):
                            color = (0, 0, 0)
                        elif isinstance(org, Zolw):
                            color = (63, 119, 84)
                        elif isinstance(org, Jagody):
                            color = (122, 52, 124)
                        elif isinstance(org, Barszcz):
                            color = (124, 51, 51)
                        elif isinstance(org, Mlecz):
                            color = (151, 158, 33)
                        elif isinstance(org, Guarana):
                            color = (216, 93, 0)
                        elif isinstance(org, Trawa):
                            color = (0, 255, 0)
                        if isinstance(org, Jagody):
                            symbol = "Ja"
                        else:
                            symbol = nazwa[0:2]
                else:
                    color = (170, 170, 170)
                    symbol = ' '
                pygame.draw.rect(self.__screen, color,
                                 pygame.Rect(x * self.__wymiar, y * self.__wymiar, self.__wymiar, self.__wymiar))
                text = font.render(symbol, True, (255, 255, 255))
                self.__screen.blit(text, (
                    x * self.__wymiar - text.get_width() // 2 + self.__wymiar / 2,
                    y * self.__wymiar - text.get_height() // 2 + self.__wymiar / 2))

        # rysowanie konsoli, tj. tekstu z informacjami o akcji.
        i = 0
        for tekst in self.__konsola:
            text = font.render(tekst, True,
                               (255, 255, 255))
            self.__screen.blit(text, (
                0, self.__y * self.__wymiar + i * 15))
            i += 1
            if i > 10:
                break

        # właściwa instrukcja dająca wszystko na ekran
        pygame.display.flip()

    def prowadzGre(self):
        self.renderuj()
        koniec = False
        while not koniec:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pozycja_myszy = pygame.mouse.get_pos()
                    if self.__przycisk1.rect.collidepoint(pozycja_myszy):
                        try:
                            self.wczytaj("plik.txt")
                        except ValueError:
                            self.pokazKomunikat("Błędny plik!")
                            exit(1)
                        except FileNotFoundError:
                            self.pokazKomunikat("Plik zapisu nie istnieje!")
                            exit(1)
                        finally:
                            koniec = True
                    elif self.__przycisk2.rect.collidepoint(pozycja_myszy):
                        try:
                            self.zapisz("plik.txt")
                            self.pokazKomunikat("Zapis powiódł się.")
                        except Exception:
                            self.pokazKomunikat("Zapis nie powiódł się!")
                        finally:
                            koniec = True
                    elif self.__przycisk3.rect.collidepoint(pozycja_myszy):
                        self.aktywuj()
                        koniec = True
                    elif self.__przycisk4.rect.collidepoint(pozycja_myszy):
                        self.wykonajTure()
                        koniec = True
                elif event.type == pygame.QUIT:
                    exit(0)

    def aktywuj(self):
        if self.__gdzieCzlowiek is not None:
            self.__gdzieCzlowiek.aktywuj()


    # Startowanie losowo rozmieszczonych organizmów:
    def startuj(self):
        for it in range(1, 25):
            i = (it % 12) + 1
            gat = Gatunek(i)
            okay = False
            while not okay:
                try:
                    noweX, noweY = random.randint(0, self.__x - 1), random.randint(0, self.__y - 1)
                    self.stworzOrganizm(gat, noweX, noweY)
                    okay = True
                except (ValueError, OccupiedError):
                    pass
                except (FullError):  # Nie ma prawa nastąpić tutaj
                    print("Błąd inicjalizacji losowej!")
                    exit(1)
        self.__organizmy = list(self.__nowa)
        del self.__nowa[:]

    def wykonajTure(self):
        del self.__konsola[:]
        self.Sortuj()
        for org in self.__organizmy:
            if org.czyZywy():
                if org.getGatunek() == Gatunek.CZLOWIEK:
                    kierunek = self.poruszCzlowieka()
                    org.akcja(kierunek)
                else:
                    org.akcja()
                org.postarz()
        for org in self.__organizmy:
            if org.czyZywy():
                self.__nowa.append(org)
        # Po tej czyności w nowej liście będą rozmnożone + pozostałe żywe, trupy już nie
        # Przeniesiemy organizmy z nowej do właściwej listy
        self.__organizmy = list(self.__nowa)
        del self.__nowa[:]

    def stworzOrganizm(self, gatunek, x, y):
        if not self.czyWspolrzedneOk(x, y):
            raise ValueError
        if self.__liczbaOrganizmow == self.__maxOrganizmow:
            raise FullError
        if self.__mapa[x][y] is not None:
            raise OccupiedError
        if gatunek == Gatunek.ANTYLOPA:
            self.__mapa[x][y] = Antylopa(x, y, self)
        elif gatunek == Gatunek.BARSZCZ:
            self.__mapa[x][y] = Barszcz(x, y, self)
            self.__ileBarszczy += 1
        elif gatunek == Gatunek.CYBEROWCA:
            self.__mapa[x][y] = Cyberowca(x, y, self)
        elif gatunek == Gatunek.CZLOWIEK:
            if self.__gdzieCzlowiek is None:
                self.__mapa[x][y] = Czlowiek(x, y, self)
                self.__gdzieCzlowiek = self.__mapa[x][y]
            else:  # Zakładam że człowiek jest tylko jeden
                return
        elif gatunek == Gatunek.GUARANA:
            self.__mapa[x][y] = Guarana(x, y, self)
        elif gatunek == Gatunek.JAGODY:
            self.__mapa[x][y] = Jagody(x, y, self)
        elif gatunek == Gatunek.LIS:
            self.__mapa[x][y] = Lis(x, y, self)
        elif gatunek == Gatunek.MLECZ:
            self.__mapa[x][y] = Mlecz(x, y, self)
        elif gatunek == Gatunek.OWCA:
            self.__mapa[x][y] = Owca(x, y, self)
        elif gatunek == Gatunek.TRAWA:
            self.__mapa[x][y] = Trawa(x, y, self)
        elif gatunek == Gatunek.WILK:
            self.__mapa[x][y] = Wilk(x, y, self)
        elif gatunek == Gatunek.ZOLW:
            self.__mapa[x][y] = Zolw(x, y, self)
        self.__nowa.append(self.__mapa[x][y])
        self.__liczbaOrganizmow += 1

    def updatujMape(self, organizm, x, y):
        stareX, stareY = organizm.getX(), organizm.getY()
        self.__mapa[x][y] = organizm
        self.__mapa[stareX][stareY] = None

    def usunZMapy(self, org):
        self.__mapa[org.getX()][org.getY()] = None
        if org.getGatunek() == Gatunek.BARSZCZ:
            self.__ileBarszczy -= 1
        if org.getGatunek() == Gatunek.CZLOWIEK:
            self.__gdzieCzlowiek = None
        self.__liczbaOrganizmow -= 1

    def zwrocZMapy(self, x, y):
        return self.__mapa[x][y]

    def czyWspolrzedneOk(self, x, y):
        if 0 <= x < self.__x and 0 <= y < self.__y:
            return True
        else:
            return False

    def wspolrzedneBarszczu(self, cyberX, cyberY):
        if self.__ileBarszczy == 0:
            return None, None
        else:
            minKroki = None
            minX, minY = None, None
            for org in self.__organizmy:
                if org.getGatunek() == Gatunek.BARSZCZ:
                    kroki = abs(org.getX() - cyberX) + abs(org.getY() - cyberY)
                    if minKroki is None or kroki < minKroki:
                        minX = org.getX()
                        minY = org.getY()
                        minKroki = kroki
            return minX, minY

    def Sortuj(self):
        self.__organizmy.sort(reverse=True)