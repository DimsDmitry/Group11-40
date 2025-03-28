from sklearn import linear_model
from sklearn.cluster import KMeans
import numpy as np
from sklearn.linear_model import LinearRegression

'''Обучение модели - это обработка набору данных с использованием некоторого алгоритма, который позволяет анализировать
 предоставленные данные и запоминать полученные результаты, в некотором смысле делать выводы на основе свойств данных.

В Scilit-learn обучение модели происходит посредством вызова её метода `fit` в который в качестве аргумента передаётся
 набор данных обучающей выборки.'''


X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]]) # обучающая выборка
y = np.dot(X, np.array([1, 2])) + 3  # тестовая выборка

# создаём объект модели, настраиваем парметры (normalize=True)
lr = linear_model.LinearRegression()

lr.fit(X, y)

# обучаем модель, передав обучающую выборку X и тестовую выборку Y
lr = LinearRegression().fit(X, y)

# Без учителя


X = np.array([[1, 2], [1, 4], [1, 0],
             [10, 2], [10, 4], [10, 0]]) # обучающая выборка, тестовой нет

kmeans = KMeans(n_clusters=2, random_state=0) # создаём объект модели, настриваем параметры
kmeans = kmeans.fit(X) # обучаем модель

X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])  # данные для обучения

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans = kmeans.fit(X)

# тестовые или новые данные для которых мы хотим получить предсказание
test = np.array([[5, 1], [0, 3], [2, 1], [11, 1], [9, 3], [9, 1]])

y = kmeans.predict(test)  # предсказываем
print('Predict: ', y)
