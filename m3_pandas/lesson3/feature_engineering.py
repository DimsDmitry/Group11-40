import pandas as pd

from functions import set_season

df = pd.read_csv('GooglePlayStore_wild.csv')


# Очистка данных из первого задания
def set_size(size):
    if size.endswith('M'):
        return float(size[:-1])
    elif size.endswith('k'):
        return float(size[:-1]) / 1024
    return -1


df['Size'] = df['Size'].apply(set_size)


def set_installs(installs):
    if installs == '0':
        return 0
    installs = (installs[:-1].replace(',', ''))
    return int(installs)


df['Installs'] = df['Installs'].apply(set_installs)

df['Type'].fillna('Free', inplace=True)


# Замени тип данных на дробное число (float) для цен приложений ('Price')
def make_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0


df['Price'] = df['Price'].apply(make_price)
# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
df['Profit'] = df['Installs'] * df['Price']
print(df['Profit'])

print('\n' + 100 * '*' + '\n')
# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?
max_profit = df[df['Type'] == 'Paid']['Profit']
print(max_profit.max())


# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'
def split_genres(genres):
    return genres.split(';')


df['Genres'] = df['Genres'].apply(split_genres)
print(df['Genres'])
df['Number of genres'] = df['Genres'].apply(len)

# Какое максимальное количество жанров ('Number of genres') хранится в датасете?
print(df['Number of genres'].max())
# Бонусное задание Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last
# Updated') приложения. Назови его 'Season'

df['Season'] = df['Last Updated'].apply(set_season)

# Выведи на экран сезоны и их количество в датасете
print(df['Season'].value_counts())
