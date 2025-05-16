class Mapmanager:
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.colors =[(0.5, 0.3, 0.0, 1),
                  (0.2, 0.2, 0.3, 1),
                  (0.5, 0.5, 0.2, 1),
                  (0.0, 0.6, 0.0, 1)]

        # создаём основной узел карты
        self.startNew()
        # создаём строительные блоки
        self.addBlock((0, 10, 0))

    def get_color(self, z):
        """выбираем цвет каждого блока в зависимости от его высоты"""
        if z < len(self.colors):
            return self.colors[z]
        return self.colors[len(self.colors) - 1]

    def startNew(self):
        """создаёт основу для новой карты"""
        self.land = render.attachNewNode("Land")
        # Land - узел, к которому привязаны все блоки карты

    def addBlock(self, position=(0, 0, 0)):
        """загружает модель блока, назначает текстуру, устанавливает координату"""
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        # передаём координату z и получаем нужный цвет
        self.color = self.get_color(int(position[2]))
        self.block.setColor(self.color)
        # добавим тег
        self.block.setTag('at', str(position))
        # привязываем блок к карте
        self.block.reparentTo(self.land)

    def clear(self):
        """очищает карту"""
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        """загружает карту из файла"""
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y

    def findBlocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def isEmpty(self, pos):
        """позволяет найти все блоки, которые находятся по координате pos"""
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        return True

    def findHighestEmpty(self, pos):
        """ищет координаты, по которым перед нами есть пустой блок.
        это нужно, чтобы понять высоту блоков перед нами - можем ли мы на них зайти"""
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return x, y, z

    def buildBlock(self, pos):
        """ставит блок с учётом гравитации"""
        x, y, z = pos
        # узнаём координаты самого высокого блока перед нами
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new)

    def delBlock(self, pos):
        """удаляет блок в указанной позиции"""
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, pos):
        """удаляет три блока перед нами"""
        x, y, z = self.findHighestEmpty(pos)
        pos  = x, y, z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()