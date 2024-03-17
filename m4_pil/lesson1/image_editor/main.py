# подключи нужные модули PIL
from PIL import Image
from PIL import ImageFilter
# создай класс ImageEditor
class ImageEditor():
    # создай конструктор класса
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    # создай метод "открыть и показать оригинал"
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не найден!')
        self.original.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        filename = self.filename.split('.')
        filename = filename[0] + str(len(self.changed))
        rotated.save(filename)

# создай методы для редактирования оригинала

# создай объект класса ImageEditor с данными картинки-оригинала

# отредактируй изображение и сохрани результат
