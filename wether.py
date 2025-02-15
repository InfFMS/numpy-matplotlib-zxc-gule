# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
from cProfile import label
import calplot
import numpy as np
import matplotlib.pyplot as plt
from pandas import value_counts
from pyparsing import alphas
from unicodedata import category

a=np.random.randint(-10,35,365)
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
b=0
n=0
m=[]
p=0
x=[]
y=[]
h=-10
categories=[]
values=[]
g=-10
v=0
while h<36:
    categories.append(h)
    h+=1
    while g<36:
        for i in range(len(a)):
            if a[i]==g:
                v+=1
        values.append(v)
        v=0
        g+=1
for i in range(len(a)):
    x.append(i+1)
    y.append(a[i])
    b+=a[i]
    if a[i]>25:
        n+=1 #количество дней с температурой выше 25
        r = plt.Circle((i+1, a[i]), 0.45, color='red')
        axs[0].add_patch(r)
    if a[i]<0:
        p+=1
        m.append(p)
        l = plt.Circle((i+1, a[i]), 0.45, color='blue')
        axs[0].add_patch(l)
    if a[i]>0:
        p=0
b=b//365 #средняя температура за год
p=max(m) #max combo
print('Средняя температура за год:',b)
print('Количество дней с температурой выше 25:',n)
print('max combo:',p)
axs[1].bar(categories,values,color='blue', linewidth=2)
axs[1].set_title('Распределение температуры')
axs[1].set_xlabel('Температура')
axs[1].set_ylabel('Дни')
axs[0].plot(x,y,linewidth=2)
axs[0].set_title('Распределение температуры по дням')
axs[0].set_xlabel('Дни')
axs[0].set_ylabel('Температура')
plt.tight_layout()
plt.show()