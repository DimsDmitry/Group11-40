with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)

author = input('Кто написал эти строки?')
with open('quotes.txt', 'a', encoding='UTF-8') as file:
    text = '('+author+')'+'\n'
    file.write(text)

with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)


while True:
    answer = input('Хотите добавить ещё цитату? (да/нет)').lower()
    if answer == 'да':
        quote = input('Введите цитату:')
        author = input('Введите автора:')
        with open('quotes.txt', 'a', encoding='UTF-8') as file:
            file.write(quote + '\n' + '('+author+')'+'\n')
    else:
        break

with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)
