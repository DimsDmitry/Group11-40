import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')

# Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы нуждаются в очистке
# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
print(df.info())
result = df[pd.isnull(df['Rating'])]
print('Приложений у которых не указан рейтинг:', len(result))
# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
df['Rating'].fillna(-1, inplace=True)
"""inplace=True означает, что изменения будут применены к исходному DataFrame, вместо создания нового"""
print(df.info())
# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
print(df['Size'].value_counts())


# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в
# Мегабайтах.


def set_size(size):
    if size.endswith('M'):
        return float(size[:-1])
    elif size.endswith('k'):
        return float(size[:-1]) / 1024
    return -1


df['Size'] = df['Size'].apply(set_size)
print(df['Size'].value_counts())

print('\n' + 100 * '=' + '\n')
# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
tools_max = df[df['Category'] == 'TOOLS']['Size'].max()
print(tools_max)


# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
def set_installs(installs):
    if installs == '0':
        return 0
    installs = (installs[:-1].replace(',', ''))
    return int(installs)


print(df['Installs'])
df['Installs'] = df['Installs'].apply(set_installs)
print(df['Installs'])
print('\n' + 100 * '*' + '\n')
# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением.
table = df.pivot_table(index='Content Rating', columns='Type', values='Installs', aggfunc='mean')
table = round(table, 1)
print(table)
print('\n' + 100 * '_' + '\n')
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?

# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
empty_type = df[pd.isnull(df['Type'])]
print(empty_type['App'])
print(empty_type['Price'])
# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно
