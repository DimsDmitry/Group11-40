from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import NumericProperty, BooleanProperty


class Runner(BoxLayout):
    """наследник класса лэйаутов"""

    value = NumericProperty(0)  # сколько сделано перемещений?
    finished = BooleanProperty(False)  # сделаны ли все перемещения

    def __init__(self,
                 total=30, steptime=1.5, autorepeat=True, bcolor=(.33, .5, .52),
                 btext_inprogress='Приседание', **kwargs
                 ):
        super().__init__()
        self.total = total
        self.autorepeat = autorepeat
        self.btext_inprogress = btext_inprogress
        # создаём анимацию перемещения вниз-вверх
        animation1 = Animation(pos_hint={'top': 0.1}, duration=steptime / 2)
        animation2 = Animation(pos_hint={'top': 1.0}, duration=steptime / 2)
        self.animation = animation1 + animation2
        # пока выполняется анимация, работает метод next
        self.animation.on_progress = self.next
        # создадим кнопку, добавим её на объект класса (наследник лэйаута)
        self.btn = Button(size_hint=(1, 0.1), pos_hint={'top': 1.0}, background_color=bcolor)
        self.add_widget(self.btn)

    def start(self):
        """вызывается в основной части программы, запускает анимацию"""
        self.value = 0
        self.finished = False
        self.btn.text = self.btext_inprogress
        if self.autorepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        """считает приседания, увеличивает их количество, пока оно не достигло максимального"""
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                # достигли нужного кол-ва приседаний - опускаем флаг анимации
                self.animation.repeat = False
                self.finished = True
