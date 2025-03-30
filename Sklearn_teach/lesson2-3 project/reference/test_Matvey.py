import numpy as np
import pandas as pd

# Step 1 - clean
df = pd.read_csv('train.csv')
print(df.info())

df.dropna(inplace=True)
print(df.info())

df.drop('has_photo has_mobile followers_count last_seen life_main '
        'people_main occupation_name city'.split(), axis=1, inplace=True)
print(df.info())
print('\n', + 100 * '=' + '\n')


def change_bdate(row):
    bdate = row['bdate'].split('.')
    if len(bdate) == 3:
        row['bdate'] = 2025 - int(bdate[2])
    else:
        row['bdate'] = np.nan
    return row


df = df.apply(change_bdate, axis=1)
df['bdate'] = df['bdate'].fillna(df['bdate'].median())

print(df['bdate'])
print('\n', + 100 * '=' + '\n')


def change_edu_form(row):
    row = row.replace('Part-time', 0)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Full-time', 2)
    return row


df = df.apply(change_edu_form, axis=1)

print(df['education_form'])
print('\n', + 100 * '=' + '\n')


def change_edu_stat(row):
    row = row.replace('Alumnus (Specialist)', 0)
    row = row.replace('Student (Specialist)', 1)
    row = row.replace("Student (Bachelor's)", 2)
    row = row.replace("Alumnus (Bachelor's)", 3)
    row = row.replace("Alumnus (Master's)", 4)
    row = row.replace('PhD', 5)
    row = row.replace("Student (Master's)", 6)
    row = row.replace('Undergraduate applicant', 7)
    row = row.replace('Candidate of Sciences', 8)
    return row


df = df.apply(change_edu_stat, axis=1)

print(df['education_status'])
print('\n', + 100 * '=' + '\n')


def change_langs(row):
    n_langs = 0
    langs = row['langs']
    if type(langs) is not int:
        if langs[0] != 'False':
            langs = row['langs'].split(';')
            n_langs = len(langs)
        row['langs'] = n_langs
    return row


df = df.apply(change_langs, axis=1)

print(df['langs'])
print('\n', + 100 * '=' + '\n')


def change_occup_type(row):
    row = row.replace('university', 0)
    row = row.replace('work', 1)
    return row


df = df.apply(change_occup_type, axis=1)

print(df['occupation_type'])
print('\n', + 100 * '=' + '\n')

# Step 2 - create model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

X = df.drop('result', axis=1)
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

sc = StandardScaler()  # The value handler
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Using the nearest neighbor method
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# We predict based on the characteristics whether people will survive
y_pred = classifier.predict(X_test)

print('\n', + 100 * '=' + '\n')
# We will display a list of actual and predicted values, but not complete, but only 10 for evaluation:
print('The present list of results:', list(y_test[:10]))
print('Predicted list of results:', list(y_pred[:10]))
result = round(accuracy_score(y_test, y_pred) * 100, 2)
print('\nPercentage of correct predictions:', result)
print('\nConfusion matrix:', confusion_matrix(y_test, y_pred))