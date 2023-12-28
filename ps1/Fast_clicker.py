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
DARK_BLUE = (0, 0, 110)
LIGHT_RED = (252, 99, 110)
LIGHT_GREEN = (153, 207, 154)

cards = []
num_cards = 4
x = 70

start_time = time.time()
cur_time = start_time


'''Интерфейс игры'''
#надпись 'время'
time_text = Label(0, 0, 50, 50, back)
time_text.set_text('Время:', 40, DARK_BLUE)
time_text.draw(0, 0)

#счёт времени
timer = Label(40, 35, 50, 40, back)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0, 0)

#надпись 'счёт'
score_text = Label(380, 0, 50, 50, back)
score_text.set_text('Счёт:', 40, DARK_BLUE)
score_text.draw(0, 0)

#счёт очков
score = Label(410, 35, 50, 40, back)
score.set_text('0', 40, DARK_BLUE)
score.draw(0, 0)


for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x += 100

wait = 0
points = 0

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
                        points += 1
                    else:
                        # иначе перекрашиваем в красный, минус очко
                        cards[i].color(RED)
                        points -= 1

                    cards[i].fill()
                    score.set_text(str(points), 40, DARK_BLUE)
                    score.draw(0, 0)

#выигрыш и проигрыш
    new_time = time.time()

    #прошло 10 сек - мы проиграли
    if new_time - start_time >= 11:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text('ВРЕМЯ ВЫШЛО!!!', 60, DARK_BLUE)
        win.draw(110, 180)
        break

    #изменение времени
    if int(new_time) - int(cur_time) == 1:
        #если проходит 1 секунда между старым и новым временем, отображаем это на экране
        timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
        timer.draw(0, 0)
        cur_time = new_time

    #набрали 5 очков - победа
    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text('ТЫ ПОБЕДИЛ!!!', 60, DARK_BLUE)
        win.draw(110, 180)
        result_time = Label(90, 230, 250, 250, LIGHT_GREEN)

        win_text = 'Время прохождения: ' + str(int(new_time - start_time)) + ' сек'
        result_time.set_text(win_text, 40, DARK_BLUE)
        result_time.draw(0, 0)
        break


    pygame.display.update()
    clock.tick(40)
pygame.display.update()
