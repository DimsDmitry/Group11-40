for i in range(20, 5, -2):
    print(i)

text = 'В МОСКВЕ сегодня тепло'
list1 = [5, 2, 3, 5, 4, 2]

num_o = 0
for s in text:
    if s.lower() == 'о':
        num_o += 1

print('В строке букв о:', num_o)

num_5 = 0
for mark in list1:
    if mark == 5:
        num_5 += 1

print('Оценок 5', num_5)