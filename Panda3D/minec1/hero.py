import pickle


# клавиши и соответствующие им действия:
key_switch_camera = 'c'  # камера привязана/отвязана от героя
# основной игровой режим/режим наблюдателя (нельзя/можно проходить сквозь блоки):
key_switch_mode = 'z'

key_turn_left = 'n'  # поворот камеры направо (мира - налево)
key_turn_right = 'm'  # поворот камеры налево (мира - направо)

key_forward = 'w'  # шаг вперёд (куда смотрит камера)
key_back = 's'  # шаг назад
key_left = 'a'  # шаг влево
key_right = 'd'  # шаг вправо

key_up = 'e'  # шаг вверх
key_down = 'q'  # шаг вниз

key_build = 'b'  # построить блок перед собой
key_destroy = 'v'  # разрушить блок перед собой

key_savemap = 'k'
key_loadmap = 'l'



class Hero:
    """класс для создания и управления персонажем"""
    def __init__(self, pos, land):
        self.land = land
        self.mode = True  # режим прохождения сквозь всё (наблюдателя)
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)  # цвет
        self.hero.setScale(0.3)  # размер
        self.hero.setPos(pos)  # разместить по координатам
        self.hero.reparentTo(render)  # привязываем к узлу рендера
        self.cameraBind()  # привязать камеру к игроку
        self.accept_events()  # подключаем обработку нажатия клавиш

    def cameraBind(self):
        """привязать камеру к игроку"""
        base.disableMouse()  # отключаем управление мышью
        base.camera.setH(180)  # РАЗВОРОТ НА 180 градусов
        base.camera.reparentTo(self.hero)  # привязываем камеру к герою
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        """отвязать камеру от игрока"""
        pos = self.hero.getPos()  # получаем текущие коорд-ы игрока
        # размещаем камеру чуть выше игрока
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3 )
        base.camera.reparentTo(render)  # привязываем камеру к узлу рендера
        base.enableMouse()  # включаем мышь
        self.cameraOn = False

    def changeView(self):
        """отвязывает/привязывает камеру к игроку в зависимости от переменной"""
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def changeMode(self):
        """переключает игровой режим"""
        if self.mode:
            self.mode = False
            print('ОСНОВНОЙ РЕЖИМ')
        else:
            self.mode = True
            print('РЕЖИМ НАБЛЮДАТЕЛЯ')

    def turn_left(self):
        """поворот влево"""
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        """поворот вправо"""
        self.hero.setH((self.hero.getH() - 5) % 360)

    def just_move(self, angle):
        """определяет движение игрока в режиме наблюдателя"""
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        """определяет движение игрока в основном игровом режиме"""
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            # перед нами свободно, возможно надо упасть вниз
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # перед нами занято. если получится, заберёмся на блок
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                # смотрим - перед нами пусто на блок выше? если да - идём туда
                self.hero.setPos(pos)
            # если не получилось забраться, ничего не происходит. стоим на месте

    def move_to(self, angle):
        """определяет вид движения в зависимости от свойства self.mode.
        Если self.mode = True, то вызываем метод just_move, иначе метод try_move."""
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def look_at(self, angle):
        """возвращает координаты, куда переместится персонаж стоящий в точке (x, y),
        если он делает шаг в направлении angle"""
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy

        return x_to, y_to, z_from

    def check_dir(self, angle):
        """ возвращает округленные изменения координат X, Y,
        соответствующие перемещению в сторону угла angle.
        Координата Y уменьшается, если персонаж смотрит на угол 0,
        и увеличивается, если смотрит на угол 180.
        Координата X увеличивается, если персонаж смотрит на угол 90,
        и уменьшается, если смотрит на угол 270.
        угол 0 (от 0 до 20)      ->        Y - 1
        угол 45 (от 25 до 65)    -> X + 1, Y - 1
        угол 90 (от 70 до 110)   -> X + 1
        от 115 до 155            -> X + 1, Y + 1
        от 160 до 200            ->        Y + 1
        от 205 до 245            -> X - 1, Y + 1
        от 250 до 290            -> X - 1
        от 290 до 335            -> X - 1, Y - 1
        от 340                   ->        Y - 1  """
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def build(self):
        """в зависимости от режима (игровой/основной) вызывает соответствующий метод
        для установки блока"""
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        """в зависимости от режима (игровой/основной) вызывает соответствующий метод
        для удаления блока"""
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def forward(self):
        """вперёд"""
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        """назад"""
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        """влево"""
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        """вправо"""
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def up(self):
        """перемещаемся вверх, ТОЛЬКО для режима наблюдателя"""
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        """перемещаемся вниз, ТОЛЬКО для режима наблюдателя"""
        if self.mode:
            self.hero.setZ(self.hero.getZ() - 1)

    def accept_events(self):
        """привязывает клавиши к методам управления игроком"""
        base.accept(key_switch_camera, self.changeView)
        base.accept(key_switch_mode, self.changeMode)

        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_right, self.turn_right)

        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right + '-repeat', self.turn_right)
        # перемещение
        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)

        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)

        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)

        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)

        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)

        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)

        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept(key_savemap, self.land.saveMap)
        base.accept(key_loadmap, self.land.loadMap)