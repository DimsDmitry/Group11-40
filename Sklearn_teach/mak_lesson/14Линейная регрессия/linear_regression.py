'''https://www.dmitrymakarov.ru/intro/regression-14/'''

'''С учителем:
1) Регрессия
2) Классификация

Без учителя:
1) Кластеризация
'''

from sklearn.datasets import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


diab = load_diabetes()

'''Вариант 1. Загрузка из библиотеки sklearn'''
# начнем с изучения описания (без команды print() описание выведется не очень аккуратно)
print(diab.DESCR)

print(10*'@')
# посмотрим на структуру с помощью метода .keys()
print(diab.keys())

print(10*'#')
# теперь посмотрим на тип данных data и target
print(type(diab.data), type(diab.target))
print(10*'#')

# переведем данные в формат DataFrame из библиотеки Pandas
# для этого передадим функции DataFrame массив признаков boston.data
# название столбцов возьмем из boston.feature_names
diab_df = pd.DataFrame(diab.data, columns=diab.feature_names)
# выведем первые пять значений с помощью функции head()
print(diab_df.head())
print(10*'*')
# теперь добавим в таблицу целевую переменную и назовем ее MEDV
diab_df['MEDV'] = diab.target
print(diab_df.head())
print(10*'=')
print(diab_df.describe().round(2))

print(10*'-')
'''Этап 2. Предварительная обработка данных'''
# проверим, есть ли пропущенные значения
print(diab_df.isnull().sum())
print(10*'+')
'''Этап 3. Исследовательский анализ данных (Exploratory Data Analysis)'''
# посчитаем коэффициент корреляции для всего датафрейма и округлим значение
# получается корреляционная матрица
corr_matrix = diab_df.corr().round(2)
print(corr_matrix)

# мы также можем построить диаграммы рассеяния, например,
# между целевой переменной MEDV и LSTAT и RM

# подготовим данные (поместим столбцы датафрейма в переменные)
x1 = diab_df['LSTAT']
x2 = diab_df['RM']
y = diab_df['MEDV']

# зададим размер и построим первый график
plt.figure(figsize=(10, 6))
plt.scatter(x1, y)

# добавим подписи
plt.xlabel('Процент населения с низким социальным статусом', fontsize=15)
plt.ylabel('Медианная цена недвижимости, тыс. долларов', fontsize=15)
plt.title('Социальный статус населения и цены на жилье', fontsize=18)
