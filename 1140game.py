import pygame


pygame.init()

# создание окна игры
clock = pygame.time.Clock()
mw = pygame.display.set_mode((500, 500))
back = (255, 251, 252)
mw.fill(back)
BLACK = (0, 0, 0)
LIGHT_BLUE = (205, 204, 255)

class TextArea():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        '''rectangle - прямоугольник'''
        self.fill_color = color
    def set_text(self, text, fsize, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


quest_card = TextArea(120, 100, 300, 70, LIGHT_BLUE)
quest_card.set_text('Вопрос', 75)


ans_card = TextArea(120, 250, 300, 70, LIGHT_BLUE)
ans_card.set_text('Ответ', 75)

quest_card.draw(10, 10)
ans_card.draw(10, 10)

pygame.display.update()
clock.tick(40)
