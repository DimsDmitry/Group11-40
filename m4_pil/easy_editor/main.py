from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import os
from PIL import Image
from PIL.ImageQt import ImageQt  # для перевода графики из Pillow в Qt
from PIL import ImageFilter
from PIL.ImageFilter import *


def chooseWorkdir():
    # выбрать рабочую папку
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def file_filter(files, extensions):
    # проверяем, оканчивается ли имя файла на расширение картинки
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result


def showFilenamesList():
    extensions = '.jpg .jpeg .png .gif .bmp .JPG'.split()
    chooseWorkdir()
    filenames = file_filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for name in filenames:
        lw_files.addItem(name)


def showChosenImage():
    """показать выбранную картинку в приложении"""
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def loadImage(self, dir, filename):
        """при загрузке запоминаем путь и имя файла"""
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        """отобразить картинку в приложении"""
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def saveImage(self):
        # сохраняет копию файла в подпапке
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def do_bw(self):
        # сделать фото ЧБ
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip(self):
        # отразить зеркально
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_sharpen(self):
        # добавить резкости
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        # развернуть влево
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        # развернуть вправо
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


workdir = ''
# главное окно
app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

# виджеты приложения
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')

btn_dir = QPushButton('Папка')
lw_files = QListWidget()
lb_image = QLabel('Картинка')

# размещение виджетов
row = QHBoxLayout()  # основная строка 4
col1 = QVBoxLayout()  # делится на столбец 1
col2 = QVBoxLayout()  # и столбец 3

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image)
row_tools = QHBoxLayout()  # строка кнопок 2
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

workimage = ImageProcessor()  # текущая картинка для работы
btn_dir.clicked.connect(showFilenamesList)
# Применяем метод ImageProcessor для отображения превью картинки
lw_files.currentRowChanged.connect(showChosenImage)

# подключаем методы обработки фотографий к кнопкам
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)

win.show()
app.exec()
