# Подсчитай количество единиц в файле.

count1 = 0

with open('my_file.txt', 'r') as my_file:
    for string in my_file:
        string_split = string.split(' ')
        for sym in string_split:
            if int(sym) == 1:
                count1 += 1

print('Единиц в файле:', count1)

# Найди и выведи на экран 8 элемент 14 строки.
with open('my_file.txt', 'r') as my_file:
    line = my_file.readlines()
    result = line[13].split(' ')[7]
    print(result)

# Найди сумму всех элементов в файле.

summ = 0

with open('my_file.txt', 'r') as my_file:
    for string in my_file:
        string_split = string.split(' ')
        for sym in string_split:
            summ += int(sym)

print('Сумма всех чисел:', summ)

# Найди и выведи на экран сумму элементов в 3, 6, 9 и 12 строках.

summ = 0
with open('my_file.txt', 'r') as my_file:
    lines = my_file.readlines()
    for i in range(len(lines)):
        string_list = lines[i].split(' ')
        for j in range(len(string_list)):
            if i in [2, 5, 8, 11]:
                summ += int(string_list[j])

    print('Результат:', summ)

# Найди сумму максимальных элементов во всех строках!
summ = 0
with open('my_file.txt', 'r') as my_file:
    lines = my_file.readlines()
    for elem in lines:
        summ += int(max(elem))

print('Сумма равна', summ)