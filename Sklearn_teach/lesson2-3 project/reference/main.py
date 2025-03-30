import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Открытие CSV файла по пути
df = pd.read_csv('train.csv')
print(df.info())

# Убираем пропуски
df.dropna(inplace=True)
print(df.info())

# данные которые не рассматриваются - их убираем
# life_main, people_main, city, last_seen, occupation_name
df = df.drop(['life_main', 'people_main', 'city', 'last_seen', 'occupation_name'], axis=1)

# Замена текстовых данных числовыми -
# это нужно сделать, тк модели машинного обучения не работают с текстом (это математические алгоритмы)

# Схема перевода текстовых данных в числовые
# 1. Смотрим, какие вообще есть данные, чтобы понять, как перевести их в числа:
# print("bdate -", df.bdate.unique())

# 2. пишем функцию замены
# def change_...(row):
# ...
# return row

# 3. применяем функцию замены
# df = df.apply(change_bdate, axis = 1)


# print("bdate -", df.bdate.unique())


# '23.4.1990', '03.05' ...
def change_bdate(row):
    # с датами работать будем так - берем год и вычитаем его из текущего года,
    #    рез-т переводим в int ('23.4.1990' -> '1990' -> 2025 - 1990 -> 35. заменяем исходную дату на 35)
    bdate = row['bdate'].split('.')
    if len(bdate) == 3:
        row['bdate'] = 2025 - int(bdate[2])
    else:
        row['bdate'] = np.nan
    return row


df = df.apply(change_bdate, axis=1)
# Заполняем пропуски медианой
df['bdate'] = df['bdate'].fillna(df['bdate'].median())

print("education_form -", df.education_form.unique())


# ['Full-time' 'Distance Learning' 'Part-time']
def change_edu_form(row):
    # Замена формы образования кодовым числом
    row = row.replace('Full-time', 2)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Part-time', 0)
    return row


df = df.apply(change_edu_form, axis=1)

print("education_status -", df.education_status.unique())


# ['Student (Specialist)' 'Alumnus (Specialist)' 'PhD' ...
def change_edu_status(row):
    # заменяем уровень образования на числовой код по мере возрастания
    row = row.replace('Undergraduate applicant', 0)
    row = row.replace("Student (Bachelor's)", 1)
    row = row.replace("Alumnus (Bachelor's)", 2)
    row = row.replace('Student (Specialist)', 3)
    row = row.replace('Alumnus (Specialist)', 4)
    row = row.replace("Student (Master's)", 5)
    row = row.replace("Alumnus (Master's)", 6)
    row = row.replace('Candidate of Sciences', 7)
    row = row.replace('PhD', 8)
    return row


df = df.apply(change_edu_status, axis=1)

print("langs -", df.langs.unique())


# ['Русский;English' 'Русский' 'False' 'Русский;Саха тыла']
def change_langs(row):
    # будем брать кол-во известных клиенту языков
    n_langs = 0
    langs = row["langs"]
    if type(langs) is not int:
        if langs[0] != 'False':
            langs = row["langs"].split(';')
            n_langs = len(langs)
        row["langs"] = n_langs
    return row


df = df.apply(change_langs, axis=1)

print("occupation_type -", df.occupation_type.unique())


# ['university' 'work']
def change_occup_type(row):
    # меняем тип занятости на кодовое значение
    row = row.replace('university', 0)
    row = row.replace('work', 1)
    return row


df = df.apply(change_occup_type, axis=1)

print("career_start -", df.career_start.unique())


# '1996', '2004' ...
def change_career_start(row):
    # та же схема что и с датой рождения (текущий год - год начала карьеры)
    start = 0
    if row['career_start'] != 'False':
        start = 2023 - int(row['career_start'])
    row['career_start'] = start
    return row


df = df.apply(change_career_start, axis=1)

print("career_end -", df.career_end.unique())


# '1996', '2004', 'False' ...
def change_career_end(row):
    # та же схема что и с датой рождения (текущий год - год начала карьеры)
    # 'False' просто меняем на 0, карьера не окончена
    end = 0
    if row['career_end'] != 'False':
        end = 2023 - int(row['career_end'])
    row['career_end'] = end
    return row


df = df.apply(change_career_end, axis=1)

print(df.info())

# ШАГ 2 - создание модели
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


# Из основного датасета убираем данные, которые будет предсказывать наша модель
X = df.drop('result', axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

sc = StandardScaler()  # обработчик значений
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# применяем метод ближайшего соседа
classifier = KNeighborsClassifier(n_neighbors=20)
classifier.fit(X_train, y_train)

# предсказываем на основании характеристик, выживут ли люди:
y_pred = classifier.predict(X_test)

print('\n' + 100 * '#' + '\n')
# выведем список фактических и предсказанных значений, но не полный а лишь 10, для оценки:
print('Настоящий список купивших:', list(y_test[:10]))
print('Предсказанный список купивших:', list(y_pred[:10]))
result = round(accuracy_score(y_test, y_pred) * 100, 2)
print('\nПроцент правильных предсказаний:', result)
print('\nConfusion matrix:', confusion_matrix(y_test, y_pred))