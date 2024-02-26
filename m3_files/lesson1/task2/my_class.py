with open('pupils_txt.txt', 'r', encoding='utf-8') as file:
    fives = []
    lines = file.readlines()
    summ = 0
    for line in lines:
        line = line.split()
        print(line[0], line[1], '-', line[2])
        mark = int(line[2])
        summ += mark
        if mark == 5:
            fives.append(line[0])

    print('\nОтличники:\n')
    for child in fives:
        print(child)
    average = summ/len(lines)
    print('\nСредний балл:', average)
