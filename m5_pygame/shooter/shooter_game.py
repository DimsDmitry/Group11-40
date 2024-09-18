from pygame import *
from random import randint

score = 0  # сбито кораблей
lost = 0  # пропущено кораблей
goal = 30  # количество сбить, которое нужно сбить
max_lost = 3  # количество сбить, которое можно пропустить


class GameSprite(sprite.Sprite):
    """базовый класс для создания спрайтов"""

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # конструктор класса
        super().__init__()
        # каждый спрайт - это картинка
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт - это прямоугольник rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        # нарисовать персонажа
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """класс-наследник GameSprite, для создания главного героя"""

    def update(self):
        """перемещение персонажа по клавишам"""
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        """выстрел"""
        bullet = Bullet(imb_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    """класс-наследник GameSprite, для создания противника"""

    def update(self):
        """автоматическое перемещение вниз по карте"""
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдёт до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class Bullet(GameSprite):
    """класс-наследник GameSprite, для создания пули"""

    def update(self):
        """автоматическое перемещение вниз по карте"""
        self.rect.y += self.speed
        # исчезает, если дойдёт до края экрана
        if self.rect.y < 0:
            self.kill()


# подключаем музыку
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

# подключаем шрифт
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

win = font1.render('ПОБЕДА', True, (255, 255, 255))
lose = font1.render('ПОРАЖЕНИЕ', True, (191, 0, 0))

# картинки
img_back = 'galaxy.jpg'
img_hero = 'rocket.png'
img_enemy = 'ufo.png'
imb_bullet = 'bullet.png'

# окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Космический шутер')
# фон сцены
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаём спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
monsters = sprite.Group()
for i in range(5):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

# игровой цикл
finish = False  # вспомогательная переменная
run = True  # флаг цикла

while run:
    # событие "закрыть игру"
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия кнопки на пробел - спрайт стреляет
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()

    if not finish:
        # отрисовываем фон и персонажей игры
        window.blit(background, (0, 0))

        # пишем текст на экране
        text = font2.render('Счёт: ' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        # отрисовываем спрайты, воспроизводим их движение
        ship.update()
        ship.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)

        # обработка столкновения пули и противника
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        # поражение - пропустили слишком много противников, или герой столкнулся с врагом
        if lost >= max_lost or sprite.spritecollide(ship, monsters, False):
            # проиграли, ставим фон и отключаем управление спрайтами
            finish = True
            window.blit(lose, (200, 200))

        # победа - очков набрано достаточно
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()
    time.delay(50)
