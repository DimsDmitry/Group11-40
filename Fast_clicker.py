import pygame
import time
from random import randint

pygame.init()
'''создаём окно программы'''
# цвет фона
back = (244, 222, 253)
# окно программы
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()


# класс прямоугольник
class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        # обводка прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


YELLOW = (255, 255, 0)
BLUE = (80, 78, 231)
GREEN = (0, 255, 96)
RED = (254, 57, 35)

cards = []
num_cards = 4
x = 70

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x += 100

wait = 0

while True:
    if wait == 0:
        # переносим надпись
        wait = 20  # столько кадров надпись будет на одном месте
        click = randint(0, num_cards - 1)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if i == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

        # на каждом кадре проверяем клик
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i == click:
                        # если на карте на которую мы кликнули, есть надпись -
                        # перекрашиваем в зелёный, плюс очко
                        cards[i].color(GREEN)
                    else:
                        # иначе перекрашиваем в красный, минус очко
                        cards[i].color(RED)

                    cards[i].fill()

    pygame.display.update()
    clock.tick(40)
