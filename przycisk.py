import pygame

class Przycisk:

    def __init__(self, tekst,x,y):
        self.__font = pygame.font.Font(None, 18)
        self.rect = pygame.Rect(x, y, 100, 20)
        self.__color = (42,103,201)
        self.__tekst = self.__font.render(tekst, True, (255, 255, 255))

    # Właściwe renderowanie przycisku.
    def render(self, screen):
        pygame.draw.rect(screen, self.__color, self.rect)
        screen.blit(self.__tekst, (self.rect.x + 4, self.rect.y + 4))