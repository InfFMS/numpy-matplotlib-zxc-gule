from cProfile import label
import calplot
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas
a=int(input('Введите значение строки: '))
b=int(input('Введите значение столбца: '))
a=abs(a-8)
b-=1
if a<0 or a>7 or b<0 or b>7:
      print('Введенных координат не существует')
else:
      data=[[0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0]]
      fig,ax=plt.subplots()
      plt.yticks(range(8), labels=[f"{abs(i-9)}" for i in range(1, 9)])
      m=['A','B','C','D','E','F','G','H']
      plt.xticks(range(8), labels=[f"{m[i]}" for i in range(0,8)])
      plt.imshow(data, cmap='binary')
      plt.title('')
      for i in range(0,8):
            for l in range(0,8):
                  if (a==i or b==l) or (abs(a-i)==abs(b-l)):
                        r=plt.Circle((l,i),0.2,color='red')
                        ax.add_patch(r)
      r = plt.Circle((b,a), 0.4, color='blue')
      ax.add_patch(r)
      plt.show()