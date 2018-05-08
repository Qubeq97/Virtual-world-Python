from Swiat import *
import pygame
from tkinter import *
import ctypes

swiat = None




def pokazKomunikat(slowo):
    ctypes.windll.user32.MessageBoxW(0, slowo, "Wirtualny świat", 0)


def inicjuj(okno, plik=None, szer=20, wys=20, okno2=None):
    global swiat
    try:
        swiat = Swiat(plik, szer, wys)
        if okno2 is not None:
            okno2.destroy()
        okno.destroy()
    except ValueError:
        if plik is None:
            pokazKomunikat("Błędne wymiary!")
        else:
            pokazKomunikat("Błąd inicjalizacji z pliku!")
            exit(1)
    except FileNotFoundError:
        pokazKomunikat("Nie znaleziono pliku!")
    except Exception as e:
        pokazKomunikat("Błąd inicjalizacji!")
        exit(1)


def podaj(okno):
    top = Tk()

    frame1 = Frame(top)
    frame1.pack(side=TOP)
    etykieta1 = Label(frame1, text="Szerokość")
    etykieta1.pack(side=LEFT)
    szer = Entry(frame1, bd=5)
    szer.pack(side=RIGHT)

    frame2 = Frame(top)
    frame2.pack(side=TOP)
    etykieta2 = Label(frame2, text="Wysokość")
    etykieta2.pack(side=LEFT)
    wys = Entry(frame2, bd=5)
    wys.pack(side=RIGHT)

    frame3 = Frame(top)
    frame3.pack(side=BOTTOM)
    Button(frame3, text='OK', command=lambda: inicjuj(okno, None, int(szer.get()), int(wys.get()), top)).pack(
        side=BOTTOM)
    top.mainloop()


def wczytaj(okno):
    inicjuj(okno, "plik.txt")


def main():
    pygame.init()
    okno = Tk()
    Button(text='Wymiary domyslne', command=lambda: inicjuj(okno)).pack(fill=X)
    Button(text='Własne wymiary', command=lambda: podaj(okno)).pack(fill=X)
    Button(text='Wczytaj', command=lambda: wczytaj(okno)).pack(fill=X)
    Button(text='Wyjście', command=lambda: exit(0)).pack(fill=X)
    okno.protocol("WM_DELETE_WINDOW", lambda: exit(0))
    okno.mainloop()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Wirtualny świat")
    swiat.setScreen(screen)
    clock = pygame.time.Clock()
    while True:
        swiat.prowadzGre()
        clock.tick(30)


if __name__ == "__main__":
    main()
