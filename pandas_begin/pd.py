import pandas as pd

marks = [5, 4, 4, 5, 3, 2, 4]
students = 'pavel stepa victor alexey sasha misha gosha'.split()

school_11 = pd.Series(data=marks, index=students)
''' pd.Series это одномерный массив 
pd.DataFrame это таблица ( двумерный массив
'''
print(school_11)
print(school_11['sasha'])

print(pd.Series(students))

# с pd.Series разобрались это массив одномерный с индексацией

sportsman = 'Pavel Georgiy Vyacheslav'

