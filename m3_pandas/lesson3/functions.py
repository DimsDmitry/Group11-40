price1 = '0'
price2 = '$2.00'
price3 = '$3.75'


def make_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0


price1 = make_price(price1)
price2 = make_price(price2)
price3 = make_price(price3)

print(price1, price2, price3)

installs1 = '1,000,000+'
installs2 = '10,000+'
installs3 = '50,000+'


def set_installs(installs):
    if installs == '0':
        return 0
    installs = (installs[:-1].replace(',', ''))
    return int(installs)


installs1 = set_installs(installs1)
installs2 = set_installs(installs2)
installs3 = set_installs(installs3)

print(installs1, installs2, installs3)
print(type(installs1))

# 1 М = 1024 k

size1 = '624k'
size2 = '6.9M'
size3 = '99M'
size4 = 'Varies with device'


def set_size(size):
    if size.endswith('M'):
        return float(size[:-1])
    elif size.endswith('k'):
        return float(size[:-1]) / 1024
    return -1


size1 = set_size(size1)
size2 = set_size(size2)
size3 = set_size(size3)
size4 = set_size(size4)

print(size1, size2, size3, size4)

date1 = 'July 18, 2018'
date2 = 'August 26, 2014'
date3 = 'November 9, 2017'
date4 = 'January 21, 2018'
date5 = 'April 25, 2018'


def set_season(date):
    month = date.split()[0]
    seasons = {
        'Зима': 'December January February'.split(),
        'Весна': 'March April May'.split(),
        'Лето': 'June July August'.split(),
        'Осень': 'September October November'.split()
    }
    for season in seasons:
        if month in seasons[season]:
            return season
    return 'Сезон не установлен'


print(set_season(date1))
print(set_season(date2))
print(set_season(date3))
print(set_season(date4))
print(set_season(date5))
