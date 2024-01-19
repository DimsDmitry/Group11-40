from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])


def show_win():
    # правильный ответ
    win = QMessageBox()
    win.setText('Верно!\nВы выиграли Iphone 15')
    win.exec()


def show_lose():
    # неправильный ответ
    win = QMessageBox()
    win.setText('Неправильно, это Индия!\nУтешительный приз - чупа-чупс')
    win.exec()


# главное окно
main_win = QWidget()
main_win.setWindowTitle('Викторина!')
main_win.resize(400, 200)

question = QLabel('Какая страна в мире самая крупная по населению?')
btn1 = QRadioButton('Китай')
btn2 = QRadioButton('Индия')
btn3 = QRadioButton('Россия')
btn4 = QRadioButton('США')

# размещаем виджеты по лэйаутам
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment=Qt.AlignCenter)

layoutH2.addWidget(btn1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment=Qt.AlignCenter)

layoutH3.addWidget(btn3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn4, alignment=Qt.AlignCenter)

# размещаем лэйауты на экран
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

# подключаем методы к каждой из кнопок
btn1.clicked.connect(show_lose)
btn2.clicked.connect(show_win)
btn3.clicked.connect(show_lose)
btn4.clicked.connect(show_lose)

main_win.show()
app.exec()
