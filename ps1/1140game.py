import pygame
from random import randint


pygame.init()


# создание окна игры
clock = pygame.time.Clock()
mw = pygame.display.set_mode((500, 500))
back = (255, 251, 252)
mw.fill(back)
BLACK = (0, 0, 0)
LIGHT_BLUE = (205, 204, 255)


class TextArea:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        '''rectangle - прямоугольник'''
        self.fill_color = color
        # список для хранения вопросов
        self.titles = []

    def add_text(self, text):
        self.titles.append(text)

    def set_text(self, number, fsize, text_color=BLACK):
        self.text = self.titles[number]
        self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)

    def draw(self, shift_x, shift_y):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


quest_card = TextArea(120, 100, 350, 70, LIGHT_BLUE)

quest_card.add_text('Вопрос')
quest_card.add_text('Что изучаешь в Алгоритмике?')
quest_card.add_text('Какое твоё увлечение?')
quest_card.add_text('На каком языке общаются в Испании?')
quest_card.add_text('Что едят на ужин?')
quest_card.add_text('Что падает с неба?')
quest_card.set_text(0, 75)


ans_card = TextArea(120, 250, 350, 70, LIGHT_BLUE)
ans_card.add_text('Ответ')
ans_card.add_text('Python')
ans_card.add_text('Французский')
ans_card.add_text('Яблоки')
ans_card.add_text('Капли дождя')
ans_card.add_text('Жаркое с грибами')
ans_card.set_text(0, 75)

quest_card.draw(10, 10)
ans_card.draw(10, 10)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1, len(quest_card.titles)-1)
                quest_card.set_text(num, 25)

                quest_card.draw(10, 25)

            if event.key == pygame.K_a:
                num = randint(1, len(ans_card.titles) - 1)
                ans_card.set_text(num, 25)

                ans_card.draw(10, 25)

    clock.tick(40)
