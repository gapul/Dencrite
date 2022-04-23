import numpy as np
from random import random,randint
import matplotlib.pyplot as plt
from math import *
import time

a = 20
N = 600

x_list1 = []
y_list1 = []
x_list2 = []
y_list2 = []
square = 0
disappeared = 0
circle = 0
n = 0
m = 0
t = time.time()

while N != n:
  x = randint(-a,a)#イオンの開始位置を定義
  y = randint(-a,a)
  if (a/4)**2 <= x**2+y**2 <= a**2:
    x_list1.append(x)
    y_list1.append(y)
    n += 1

for num in range(0, len(x_list1)):
  m = 0
  while m == 0:
    theta=2.0*pi*random()#角度θ(2pi単位)をランダムにするため，random()を使って[0,1]の一様乱数を発生させる。
    x_list1[num] += cos(theta) # x方向への移動。cos(θ)
    y_list1[num] += sin(theta)# y方向への移動。sin(θ)
    if (x_list1[num])**2+(y_list1[num])**2<=(a/4)**2:#金属板に触れたイオンを析出
      x_list2.append(x_list1[num])
      y_list2.append(y_list1[num])
      square+=1
      print("sq")
      m = 1
    elif abs(x_list1[num]+y_list1[num])+abs(x_list1[num]-y_list1[num])>=a*3:#離れていったイオンを排除
      disappeared+=1
      print("dis")
      m = 1
    elif len(x_list2)<=0 :
      m = 0
    else:
      if min(x_list2)-1<=x_list1[num] and x_list1[num]<=max(x_list2)+1 and min(y_list2)-1<=y_list1[num] and y_list1[num]<=max(y_list2)+1:
        for cx in x_list2:
          if (x_list1[num]-cx)**2+(y_list1[num]-y_list2[x_list2.index(cx)])**2<=1:#新たに析出したスズに触れたイオンを析出
            x_list2.append(x_list1[num])
            y_list2.append(y_list1[num])
            circle+=1
            print("circ")
            m = 1
            break
        
print(x_list2)
print(y_list2)
print("------------------------------------------------")
print("time:"+str(time.time()-t))
print("square:"+str(square))
print("disappeared:"+str(disappeared))
print("circle:"+str(circle))
# for plot
fig = plt.figure(figsize=(5,5))#出力サイズ
ax = fig.add_subplot(1,1,1)#グラフのサイズ
plt.scatter(x_list2,y_list2)# (x,y)の散布図
rec=plt.Circle((0,0),a/4,fill=False)#図形の定義
ax.add_patch(rec)#四角形の描写の追加
plt.xlabel('X') # x軸のラベル
plt.ylabel('Y') # y軸のラベル
plt.xlim([-a,a]) # x軸の範囲
plt.ylim([-a,a])#y軸の範囲
plt.show()
