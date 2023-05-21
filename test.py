import pygame
from random import *

pygame.init()

clock = pygame.time.Clock()
mw = pygame.display.set_mode((500, 500))
back = (255, 251, 252)
mw.fill(back)
BLACK = (0, 0, 0)
light_red = (246, 172, 172)

class TextArea:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def set_text(self, text, fsize, text_color = BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


quest_card = TextArea(120, 100, 300, 70, light_red)
quest_card.set_text("Вопрос", 75)

ans_card = TextArea(120, 350, 300, 70, light_red)
ans_card.set_text('Ответ', 75)

quest_card.draw(10, 10)
ans_card.draw(10, 10)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.key == pygame.k_q:
                num = randint(1, 3)
                if num == 1:
                    quest_card.set_text('КТО ЕСТ БАНАНА')
                if num == 2:
                    quest_card.set_text('ЧТО ТАКОЕ КУБИКА')
                if num == 3:
                    quest_card.set_text('КТО ТАКОЙ АШОТИК')
                quest_card.draw(10, 25)

            if event.type == pygame.MOUSEBUTTON:
                if event.key == pygame.k_q:
                    number = randint(1, 3)
                    if num == 1:
                        ans_card.set_text('бобизяны')
                    if num == 2:
                        ans_card.set_text('ягода')
                    if num == 3:
                        ans_card.set_text('крутой челик')
    clock.tick(40)