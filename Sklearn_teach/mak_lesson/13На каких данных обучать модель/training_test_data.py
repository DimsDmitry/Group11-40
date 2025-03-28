'''https://www.dmitrymakarov.ru/intro/train-test-13/#1-obuchayushchaya-i-testovaya-vyborki'''

# возьмем данные роста (X) и обхвата шеи (y)
X = [1.48, 1.49, 1.49, 1.50, 1.51, 1.52, 1.52, 1.53, 1.53, 1.54, 1.55, 1.56, 1.57, 1.57, 1.58, 1.58, 1.59, 1.60, 1.61,
     1.62, 1.63, 1.64, 1.65, 1.65, 1.66, 1.67, 1.67, 1.68, 1.68, 1.69, 1.70, 1.70, 1.71, 1.71, 1.71, 1.74, 1.75, 1.76,
     1.77, 1.77, 1.78]
y = [29.1, 30.0, 30.1, 30.2, 30.4, 30.6, 30.8, 30.9, 31.0, 30.6, 30.7, 30.9, 31.0, 31.2, 31.3, 32.0, 31.4, 31.9, 32.4,
     32.8, 32.8, 33.3, 33.6, 33.0, 33.9, 33.8, 35.0, 34.5, 34.7, 34.6, 34.2, 34.8, 35.5, 36.0, 36.2, 36.3, 36.6, 36.8,
     36.8, 37.0, 38.5]

# print(len(X), len(y))
# импортируем библиотеку Numpy
import numpy as np

# преобразуем наш список X сначала в одномерный массив Numpy, а затем добавим второе измерение
X = np.array(X).reshape(-1, 1)
# print(X)
# список y достаточно преобразовать в одномерный массив Numpy
# y = np.array(y)
print(y)
# из модуля model_selection библиотеки sklearn импортируем функцию train_test_split
from sklearn.model_selection import train_test_split

# разбиваем данные на четыре части
# названия переменных могут быть любыми, но обычно используют именно их
# также задаем размер тестовой выборки (30%) и точку отсчета для воспроизводимости
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=41)

print(X.shape)
# теперь посмотрим, что сделала функция train_test_split
print(X_train.shape, X_test.shape)


'''Далее мы снова построим нашу модель, но уже с учетом вышеописанного разделения на train и test
(для простоты часто говорят именно так).'''

# из набора линейных моделей библиотеки sklearn импортируем линейную регрессию
from sklearn.linear_model import LinearRegression


# создадим объект этого класса и запишем в переменную model
model = LinearRegression()

# обучим нашу модель
# т.е. найдем те самые веса или наклон и сдвиг прямой с помощью функции потерь
# только теперь используем только обучающую выборку
model.fit(X_train, y_train)


# выведем наклон и сдвиг с помощью атрибутов coef_ и intercept_ соответственно
print(model.coef_, model.intercept_)


# Сделаем прогноз, но уже на тестовой выборке.

# на основе значений роста (Х) предскажем значения обхвата шеи
y_pred = model.predict(X_test)

# выведем первые пять значений с помощью диапазона индексов
print(y_pred[:5])
print(y_test[:5])

# импортируем модуль метрик
from sklearn import metrics

# выведем корень среднеквадратической ошибки
# в этот раз сравним тестовые и прогнозные значения окружности шеи
print('Root Mean Squared Error (RMSE):', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
