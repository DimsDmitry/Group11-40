import pygame
import time


pygame.init()
'''создаём окно программы'''
#цвет фона
back = (244, 222, 253)
#окно программы
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

#класс прямоугольник
class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        #обводка прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)


class Label(Area):
    def set_text(self, text, fsize, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


YELLOW = (255, 255, 0)
BLUE = (80, 78, 231)

cards = []
num_cards = 4
x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x += 100

