import pandas as pd
import numpy as np
df = pd.read_csv('/home/vladislav/PycharmProjects/NMPract1/data/adult.data.csv')
print('Task №1')
print('Кількість чоловіків: ' + str(df[df['sex'] == 'Male']['sex'].count()))
print('Кількість жінок: ' + str(df[df['sex'] == 'Female']['sex'].count()))

print('\n Task №2 ')
print('Cередній вік жінок: ' + str(df[df['sex'] == 'Female']['age'].mean()))

print('\n Task №3')
print('Частка громадян Німеччини: ' + str((df[df['native-country'] == 'Germany']['native-country'].count() / len(df.index) * 100)) + '%')

print('\n Task №4 ')
print('Середнє значення  віку >50K: ' + str(df[df['salary'] == '>50K']['age'].mean()))
print('Cередньоквадратичнe відхилення віку >50K: ' + str(df[df['salary'] == '>50K']['age'].std()))
print('Середнє значення  віку <=50K: ' + str(df[df['salary'] == '<=50K']['age'].mean()))
print('Cередньоквадратичнe відхилення віку <=50K: ' + str(df[df['salary'] == '<=50K']['age'].std()))

print('\n Task №5')
task5 = df[(df['salary'] == '<=50K') & ((df['education'] == 'Bachelors') | (df['education'] == 'Prof-school') |
                                     (df['education'] == 'Assoc-voc') | (df['education'] == 'Masters') |
                                     (df['education'] == 'Doctorate'))]['education'].count()
if task5 != 0 : print("Люди, які отримують більше 50К, мають як мінімум вищу освіту це брехня")
else: print('Люди, які отримують більше 50К, мають як мінімум вищу освіту це правда')

print('\n Task №6')
for (race, sex), sub_df in df.groupby(['race', 'sex']):
    print("Race: {0}, sex: {1}".format(race, sex))
    print(sub_df['age'].describe())


print('\n Task №7')
print('Заробітна плата неодружених чоловіків')
print(df.loc[(df['sex'] == 'Male') & (df['marital-status'].isin(['Never-married',
                                   'Separated',
                                   'Divorced',
                                   'Widowed'])), 'salary'].value_counts())

print('Заробітна плата одружених чоловіків')
print(df.loc[(df['sex'] == 'Male') &
     (df['marital-status'].str.startswith('Married')), 'salary'].value_counts())

print('\n Task №8')
print('Максимальна кількість годин людина працює на тиждень: ' + str(df['hours-per-week'].max()))

num_whs = df[df['hours-per-week'] == df['hours-per-week'].max()].shape[0]
print("Людей, які працюють максимальну кількість годин {0}".format(num_whs))

rich_share = float(df[(df['hours-per-week'] == df['hours-per-week'].max())
                 & (df['salary'] == '>50K')].shape[0]) / num_whs
print("Відсоток людей, які заробляють багато {0}%".format(int(100 * rich_share)))

print('\n Task №9')
for (country, salary), sub_df in df.groupby(['native-country', 'salary']):
    print(country, salary, round(sub_df['hours-per-week'].mean(), 2))