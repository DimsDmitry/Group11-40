import pandas as pd

# ШАГ 1 - подготовка и очистка данных
df = pd.read_csv('titanic.csv')
print(df.groupby('Sex')['Survived'].mean())
df.drop('PassengerId Name Ticket Cabin Embarked'.split(), axis=1, inplace=True)
print(df.info())
# узнаем зависимость класса от возраста
average_age = df.groupby('Pclass')['Age'].median()
# заполним пропущенные значения возраста в зависимости от класса
age1 = average_age[1]
print(age1)  # средний возраст в 1 классе
age2 = average_age[2]
print(age2)  # средний возраст во 2 классе
age3 = average_age[3]
print(age3)  # средний возраст в 3 классе


def fill_age(row):
    """функция вставляющая в пустое поле значение возраста, на основании класса"""
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age1
        if row['Pclass'] == 2:
            return age2
        return age3
    return row['Age']


df['Age'] = df.apply(fill_age, axis=1)  # применяем функцию замены ко всему столбцу Age
print(df.info())  # Проверяем результат. Замена прошла успешно


def fill_sex(sex):
    """функция заменяющая пол человека под число"""
    if sex == 'male':
        return 1
    return 0


df['Sex'] = df['Sex'].apply(fill_sex)  # применяем функцию замены ко всему столбцу Sex

print(df['Sex'])

# ШАГ 2 - создание модели
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

sc = StandardScaler()  # обработчик значений
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# применяем метод ближайшего соседа
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# предсказываем на основании характеристик, выживут ли люди:
y_pred = classifier.predict(X_test)

print('\n' + 100 * '#' + '\n')
# выведем список фактических и предсказанных значений, но не полный а лишь 10, для оценки:
print('Настоящий список выживших:', list(y_test[:10]))
print('Предсказанный список выживших:', list(y_pred[:10]))
result = round(accuracy_score(y_test, y_pred) * 100, 2)
print('\nПроцент правильных предсказаний:', result)
print('\nConfusion matrix:', confusion_matrix(y_test, y_pred))