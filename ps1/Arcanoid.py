import pygame

pygame.init()

back = (200, 255, 255)  # цвет фона (background)
mw = pygame.display.set_mode((500, 500))  # окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()

# переменные, отвечающие за координаты платформы
racket_x = 200
racket_y = 330

# флаги движения платформы
move_right = False
move_left = False

# переменные, отвечающие за движение мяча
dx = 3
dy = 3

# флаг окончания игры
game_over = False


# класс из предыдущего проекта
class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


# класс для надписей
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


# класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


# создание мяча и платформы
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)

# создание врагов
start_x = 5  # координаты создания первого монстра
start_y = 5
count = 9  # количество монстров в верхнем ряду
monsters = []  # список для хранения объектов-монстров
for j in range(3):  # цикл по столбцам
    y = start_y + (55 * j)  # координата монстра в каждом след. столбце будет смещена на 55 пикселей по y
    x = start_x + (27.5 * j)  # и 27.5 по x
    for i in range(count):  # цикл по рядам (строкам) создаёт в строке количество монстров, равное count
        d = Picture('enemy.png', x, y, 50, 50)  # создаём монстра
        monsters.append(d)  # добавляем в список
        x = x + 55  # увеличиваем координату следующего монстра
    count = count - 1  # для следующего ряда уменьшаем кол-во монстров

while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # если нажата стрелка
                move_right = True  # поднимаем флаг
            if event.key == pygame.K_LEFT:
                move_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:  # если отпущена стрелка
                move_right = False  # опускаем флаг
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:  # флаг движения вправо
        platform.rect.x += 3
    if move_left:  # флаг движения влево
        platform.rect.x -= 3

    # придаём мячу постоянную скорость по x и y
    ball.rect.x += dx
    ball.rect.y += dy

    # если координата Y мяча достигает 350 - поражение
    if ball.rect.y > 350:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('ТЫ ПРОИГРАЛ', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True

    # закончились монстры - победа
    if len(monsters) == 0:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text('ПОБЕДА', 60, (28, 202, 0))
        time_text.draw(10, 10)
        game_over = True

    # если мяч достигает границы экрана, меняем его направление
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1
    # касание платформы
    if ball.rect.colliderect(platform.rect):
        dy *= -1

    # отрисовываем всех монстров из списка
    for m in monsters:
        m.draw()
        # если мяч коснулся монстра - удаляем его из списка и меняем направление мяча
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1

    platform.draw()
    ball.draw()

    pygame.display.update()

    clock.tick(40)