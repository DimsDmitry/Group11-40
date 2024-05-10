from pygame import *


class GameSprite(sprite.Sprite):
    """базовый класс для создания спрайтов"""

    def __init__(self, player_image, player_x, player_y, player_speed):
        # конструктор класса
        super().__init__()
        # каждый спрайт - это картинка
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # каждый спрайт - это прямоугольник rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        # нарисовать персонажа
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """класс-наследник GameSprite, для создания управляемого персонажа"""

    def update(self):
        """перемещение персонажа по клавишам"""
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed


class Enemy(GameSprite):
    """класс-наследник GameSprite, для создания спрайта-врага (перемещается сам)"""
    direction = 'left'

    def update(self):
        """автоматическое перемещение персонажа"""
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 80:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    """класс-наследник встроенного в PyGame класса Sprite, для создания стены"""

    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        # стена - прямоугольник размеров width и height
        self.image = Surface((self.width, self.height))
        # заливаем полученную поверхность цветом
        self.image.fill((color1, color2, color3))
        # каждый спрайт хранит свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        """нарисовать стену"""
        window.blit(self.image, (self.rect.x, self.rect.y))


# окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
# фон сцены
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
# персонажи игры
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 300, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(150, 205, 50, 100, 20, 450, 10)
w2 = Wall(150, 205, 50, 100, 480, 350, 10)
w3 = Wall(150, 205, 50, 100, 20, 10, 380)

# музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

# текст
font.init()
font = font.Font(None, 70)
win = font.render('ПОБЕДА!', True, (247, 255, 0))
lose = font.render('ПОРАЖЕНИЕ!', True, (255, 0, 50))

# игровой цикл
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        # отрисовываем фон и персонажей игры
        window.blit(background, (0, 0))

        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        # поражение
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) \
                or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        # победа
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)
