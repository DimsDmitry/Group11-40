import pandas as pd
import numpy as np
from numpy.ma.extras import average

# ШАГ 1 - ПОДГОТОВКА И ОТЧИСТКА ДАННЫХ

df = pd.read_csv('train.csv')
print(df.info())

df.dropna(inplace=True)

df = df.drop('life_main people_main city last_seen occupation_type langs'.split(), axis=1)

def change_bdate(row):
    bdate = row['bdate'].split('.')
    if len(bdate) == 3:
        row['bdate'] = 2023 - int(bdate[2])
    else:
        row['bdate'] = np.nan
    return row

df = df.apply(change_bdate, axis=1)

df['bdate'] = df['bdate'].fillna(df['bdate'].median())


print('education_form-', df.education_form.unique())

def change_edu_form(row):
    row = row.replace('Full-time', 2)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Part-time', 0)
    return row

df = df.apply(change_edu_form, axis=1)


print('education_status-', df.education_status.unique())

def change_edu_status(row):
    row = row.replace('Undergraduate applicant', 0)
    row = row.replace("Student (Bachelor's)", 1)
    row = row.replace("Alumnus (Bachelor's)",2)
    row = row.replace("Student (Specialist)", 3)
    row = row.replace("Alumnus (Specialist)", 4)
    row = row.replace("Student (Master's)", 5)
    row = row.replace("Alumnus (Master's)", 6)
    row = row.replace("Candidate of Sciences", 7)
    row = row.replace("PhD", 8)
    return row

df = df.apply(change_edu_status, axis=1)


def change_occup_type(row):
    row = row.replace('university', 0)
    row = row.replace('work', 1)
    return row

df = df.apply(change_occup_type, axis=1)


print('career_end-', df.career_end.unique())

def change_career_end(row):
    end = 0
    if row['career_end'] != 'False':
        end = 2023 - int(row['career_end'])
    else:
        return 0
    return row

df = df.apply(change_career_end, axis=1)

def change_car_start(row):
    row = row.replace('False', 0)
    return row

df = df.apply(change_car_start, axis=1)


def change_car_end(row):
    end = 0
    if row['career_end'] != 'False':
        end = 2023 - int(row['career_end'])
    row['career_end'] = end
    return row

df = df.apply(change_car_end, axis=1)

# ШАГ 2 - СОЗДАНИЕ МОДЕЛИ

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metricstrics import confusion_matrix, accuracy_score

X = df.drop('result', axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=20)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print('The present list of results:', list(y_test[:10]))
print('Predicted:', list(y_pred[:10]))
result = round(accuracy_score(y_test, y_pred) * 100, 2)
print('percentage of cor:', result)
print('Conf matrix:', confusion_matrix(y_test, y_pred))