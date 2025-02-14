import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
result = df['Category'].value_counts()['BUSINESS']
print(result)


# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
unique = df['Content Rating'].value_counts()
res1 = unique['Teen']
res2 = unique['Everyone 10+']
result = round(res1/res2, 2)
print(result)
print('\n' + 100 * '=' + '\n')
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.
res = df.groupby(by='Type')['Rating'].mean()
print(round(res['Paid'], 2))

# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
print(round(res['Paid'] - res['Free'], 2))
print('\n' + 100 * '=' + '\n')
# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
result = df.groupby(by='Category')['Size'].agg(['min', 'max'])
print(result)
print('\n' + 100 * '=' + '\n')
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
result = df[df['Rating'] > 4.5]['Category'].value_counts()['FINANCE']
print(result)
print('\n' + 100 * '#' + '\n')

# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
result = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
res = result['Free']/result['Paid']
print(res)
