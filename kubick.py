# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
from cProfile import label
import calplot
import numpy as np
import matplotlib.pyplot as plt
from pandas import value_counts
from pyparsing import alphas
fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # 1 ряд, 2 столбца
categories=['1','2','3','4','5','6','max combo']
categories1=['1','2','3','4','5','6']
a=np.random.randint(1,7,1000)
q=0
w=0
e=0
r=0
t=0
y=0
p=[1]
u=0
z=1
for i in range(0,1000):
    if a[i]==1:
        q+=1
    elif a[i]==2:
        w+=1
    elif a[i]==3:
        e+=1
    elif a[i]==4:
        r+=1
    elif a[i]==5:
        t+=1
    elif a[i]==6:
        y+=1
for i in range(0,999):
    u = a[i + 1]
    if u==a[i]:
        z+=1
        p.append(z)
    else:
        z=1

u=max(p)
values=(q,w,e,r,t,y,u)
values1=(q/10,w/10,e/10,r/10,t/10,y/10)

axs[0].set_title('Количество выпавших зачений')
axs[0].bar(categories,values,color='blue',linewidth=2)
axs[1].set_title('Вероятность выпадения в %')
axs[1].bar(categories1,values1,color='blue',linewidth=2)
plt.show()