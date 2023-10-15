import pygame

pygame.init()

back = (200, 225, 250)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

racket_x = 200
racket_y = 330

move_right = False
move_left = False

dx = 3
dy = 3

game_over = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thikness):
        # обводка прямоугольника
        pygame.draw.rect(mw, frame_color, self.rect, thikness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x, y, width, height):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('Verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)

start_x = 5
start_y = 5
count = 9

monsters = []
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)

    for i in range(count):
        demon = Picture('enemy.png', x, y, 50, 50)
        monsters.append(demon)
        x = x + 55
    count = count - 1

while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False

    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y > 350:
        time_text = Label(90, 150, 50, 50, back)
        time_text.set_text('ТЫ ПОИГРАЛ!!!', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True

    if len(monsters) == 0:
        time_text = Label(90, 150, 50, 50, back)
        time_text.set_text('ПОБЕДА!!!', 60, (0, 250, 0))
        time_text.draw(10, 10)
        game_over = True

    if ball.rect.y <= 0:
        dy *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    if ball.rect.colliderect(platform.rect):
        dy *= -1

    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            dy *= -1

    platform.draw()
    ball.draw()

    pygame.display.update()

    clock.tick(40)
