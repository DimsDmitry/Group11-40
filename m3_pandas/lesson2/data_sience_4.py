import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с
# точностью до десятых.
res = df.groupby(by='Type')['Rating'].agg('min mean max'.split())
res = round(res, 1)
print(res)

print('\n' + 100 * '=' + '\n')
# 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid')
# для разных целевых аудиторий ('Content Rating')
result = df[df['Type'] == 'Paid'].groupby(by='Content Rating')['Price'].agg('min median max'.split())
print(result)
print('\n' + 100 * '-' + '\n')
# 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
# посчитай максимальное количество отзывов ('Reviews') в каждой группе.
# Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
# В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?
# Подсказка: ты можешь выбрать из DataFrame несколько столбцов одновременно с помощью такого синтаксиса:
# df[[<столбец 1>, <столбец 2>, <столбец 3>]]
res = df.pivot_table(index='Content Rating', columns='Category', values='Reviews', aggfunc='max')
print(res['EDUCATION FAMILY GAME'.split()])

print('\n' + 100 * '*' + '\n')
# 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
# Посчитай среднее количество отзывов ('Reviews') в каждой группе Обрати внимание, что в некоторых ячейках полученной
# таблицы отражается не число, а значение "NaN" - Not a Number Эта запись означает, что в данной группе нет ни одного
# приложения. Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в
# алфавитном порядке.

res = df[df['Type'] == 'Paid'].pivot_table(index='Category', columns='Content Rating', values='Reviews', aggfunc='mean')
print(res)

print('\n' + 100 * '-' + '\n')
# Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений, 
# в которых приложения разработаны не для всех возрастных групп ('Content Rating')

res = df[df['Type'] == 'Free'].pivot_table(index='Category', columns='Content Rating', values='Reviews', aggfunc='mean')
print(res)