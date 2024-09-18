for i in range(5):
    password = input('Введите пароль: ')
    if password == '123':
        print('Доступ получен!')
        break

marks = [5, 2, 3, 5, 'hello', 2, 3, 5]
summ = 0

for m in marks:
    try:
        summ += m
    except TypeError:
        continue

print('Сумма всех оценок:', summ)
