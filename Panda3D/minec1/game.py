from direct.showbase.ShowBase import ShowBase

from mapmanager import Mapmanager
from hero import Hero


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # создаём карту, загружаем её, получаем её координаты
        self.land = Mapmanager()
        x, y = self.land.loadLand('land.txt')
        # создаём игрока
        self.hero = Hero((x//2, y//2, 2), self.land)
        base.camLens.setFov(90)

app = MyApp()
app.run()
