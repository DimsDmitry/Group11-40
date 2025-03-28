# Мы можем загружать данные (датасеты, datasets)  извне, например, из **txt, csv, json файлов и т.д.с помощью Pandas:
import numpy as np
import pandas as pd


loaded_data = pd.read_csv('titanic.csv', sep='\t')
# первые 3 строки
print(loaded_data.head(3))

print(100 * '#')

X = np.random.random((10, 5))
# для простоты эксперимента просто сгенерируем случайные числа
# строим 10 строк по 5 столбцов случайных чисел
print(X)

print(100 * '#')

# Нормализация (Normalization)
