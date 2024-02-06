from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle


class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


# создаём список вопросов, сами вопросы, добавляем их в список
question_list = []
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Бразильский', 'Испанский')
q2 = Question('Какого цвета нет на флаге России?', 'Зелёный', 'Белый', 'Синий', 'Красный')
q3 = Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Хата', 'Иглу')

question_list.append(q1)
question_list.append(q2)
question_list.append(q3)

app = QApplication([])

# окно приложения
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 300)

# интерфейс приложения
btn_OK = QPushButton('Ответить')

lbl_question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответов')
# группа на экране для переключателей с ответами

btn_1 = QRadioButton('Вариант 1')
btn_2 = QRadioButton('Вариант 2')
btn_3 = QRadioButton('Вариант 3')
btn_4 = QRadioButton('Вариант 4')

# группируем переключатели ответов
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
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('текст')  # здесь будет надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ')  # а здесь будет правильный ответ

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()  # вопрос
layout_line2 = QHBoxLayout()  # варианты ответов или результат теста
layout_line3 = QHBoxLayout()  # кнопка "Ответить"

layout_line1.addWidget(lbl_question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
# скроем панель ответов, потому что сначала высвечивается панель вопросов:
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # кнопку ответа делаем побольше
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым


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


def ask(q):
    # функция записывает значения вопроса и ответов в нужные виджеты. Ответы перемешиваются
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl_question.setText(q.question)  # вопрос
    lb_Correct.setText(q.right_answer)  # ответ
    show_question()  # показываем панель вопросов


def show_correct(res):
    # установим текст в надпись "результат" и покажем нужную панель
    lbl_question.setText(res)
    show_result()


def check_answer():
    # проверяет вариант ответа, показывает панель ответов
    if answers[0].isChecked():
        show_correct('Верно!')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')


def next_question():
    # задаёт следующий вопрос из списка
    window.cur_question += 1  # переход к следующему вопросу
    if window.cur_question >= len(question_list):
        window.cur_question = 0  # если список вопросов кончился - идём сначала
    q = question_list[window.cur_question]
    ask(q)


def click_OK():
    # определяет, надо показывать другой вопрос или проверить ответ на этот
    if btn_OK.text() == 'Ответить':
        check_answer()  # проверка ответа
    else:
        next_question()  # следующий вопрос


window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1

btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec()
