from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os


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
    extensions = '.jpg .jpeg .png .gif .bmp'.split()
    chooseWorkdir()
    filenames = file_filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for name in filenames:
        lw_files.addItem(name)


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

btn_dir.clicked.connect(showFilenamesList)
win.show()
app.exec()
