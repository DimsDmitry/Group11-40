from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

app = QApplication([])

# окно приложения
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(800, 600)

# интерфейс приложения
btn_OK = QPushButton('Ответить')

lbl1 = QLabel('В каком году основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')
# группа на экране для переключателей с ответами

btn_1 = QRadioButton('Вариант 1')
btn_2 = QRadioButton('Вариант 2')
btn_3 = QRadioButton('Вариант 3')
btn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(btn_1)
RadioGroup.addButton(btn_2)
RadioGroup.addButton(btn_3)
RadioGroup.addButton(btn_4)

# линии для размещения виджетов
line_ans1 = QHBoxLayout()
line_ans2 = QVBoxLayout()
line_ans3 = QVBoxLayout()
# вертикальные линии будут внутри горизонтальной. На горизонтальные добавляем кнопки
line_ans2.addWidget(btn_1)
line_ans2.addWidget(btn_2)
line_ans3.addWidget(btn_3)
line_ans3.addWidget(btn_4)
# разместили столбцы в одной линии
line_ans1.addLayout(line_ans2)
line_ans1.addLayout(line_ans3)
# панель с вариантами ответов
RadioGroupBox.setLayout(line_ans1)
line_h1 = QHBoxLayout()  # вопрос
line_h2 = QHBoxLayout()  # варианты ответов (или результат теста)
line_h3 = QHBoxLayout()  # кнопка "Ответить"

# добавляем виджеты
line_h1.addWidget(lbl1, alignment=Qt.AlignCenter)
line_h2.addWidget(RadioGroupBox)
line_h3.addWidget(btn_OK, stretch=2)  # делаем кнопку больше

# создадим главный лэйаут, разместим остальные лэйауты на нём
layout_card = QVBoxLayout()

layout_card.addLayout(line_h1, stretch=2)
layout_card.addLayout(line_h2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(line_h3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Здесь будет ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()


def show_result():
    # показать панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    # показать панель вопросов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)  # снимаем ограничения, чтобы можно было сбросить кнопку
    btn_1.setChecked(False)
    btn_2.setChecked(False)
    btn_3.setChecked(False)
    btn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # вернули ограничения, теперь может быть выбрана только одна кнопка


answers = [btn_1, btn_2, btn_3, btn_4]


def ask(question, right_answer, wrong1, wrong2, wrong3):
    # функция записывает значения вопроса и ответов в нужные виджеты. Ответы перемешиваются
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lbl1.setText(question)
    lb_Correct.setText(right_answer)
    show_question()


def show_correct(res):
    # установим текст в надпись "результат" и покажем нужную панель
    lbl1.setText(res)
    show_result()


def check_answer():
    # проверяет вариант ответа, показывает панель ответов
    if answers[0].isChecked():
        show_correct('Верно!')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')


ask('Государственный язык Бразилии?', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')


btn_OK.clicked.connect(check_answer)
window.setLayout(layout_card)
window.show()
app.exec()
