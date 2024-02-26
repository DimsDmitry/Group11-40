with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)

author = input('Кто написал эти строки?')
with open('quotes.txt', 'a', encoding='UTF-8') as file:
    text = '('+author+')'+'\n'
    file.write(text)

while True:
    answer = input('Хотите добавить ещё цитату? (да/нет)').lower()
    if answer == 'да':
        quote = input('Введите цитату:')
        author = input('Введите автора:')
        file = open('quotes.txt', 'a', encoding='UTF-8')
        file.write(quote + '\n' + '('+author+')'+'\n')
        file.close()
    else:
        break

with open('quotes.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    print(text)
