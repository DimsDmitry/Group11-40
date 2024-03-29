# подключи нужные модули PIL
from PIL import *
from PIL import ImageFilter
from PIL import Image


# создай класс ImageEditor
class ImageEditor:
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

    # создай методы для редактирования оригинала
    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        filename = self.filename('.')
        filename = filename[0] + str(len(self.changed))
        rotated.save(filename)

    def do_cropped(self):
        box = (100, 100, 400, 450)
        cropped = self.original.crop(box)
        self.changed.append(cropped)

        filename = self.filename('.')
        filename = filename[0] + str(len(self.changed))
        cropped.save(filename)


# создай объект класса ImageEditor с данными картинки-оригинала
photo = ImageEditor('original')
# отредактируй изображение и сохрани результат
photo.open()
photo.do_left()
photo.do_cropped()
