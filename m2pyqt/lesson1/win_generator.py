from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

# главное окно
my_win = QWidget()
my_win.setWindowTitle('Определитель победителя')
my_win.move(100, 100)
my_win.resize(400, 200)

# виджеты - кнопка и надпись
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

# расположение виджетов
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)

my_win.setLayout(line)

my_win.show()
app.exec()
