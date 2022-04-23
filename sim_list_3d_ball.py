import numpy as np
from random import random,randint
import matplotlib.pyplot as plt
from math import *
import time
from mpl_toolkits.mplot3d.axes3d import Axes3D

a = 20
N = 900

x_list1 = []
y_list1 = []
z_list1 = []
x_list2 = []
y_list2 = []
z_list2 = []
square = 0
disappeared = 0
circle = 0
n = 0
m = 0
t = time.time()

while N != n:
  x = randint(-a,a)#イオンの開始位置を定義
  y = randint(-a,a)
  z = randint(-a,a)
  if  (a/4)**2 <= x**2+y**2+z**2 <= a**2:
    x_list1.append(x)
    y_list1.append(y)
    z_list1.append(z)
    n += 1

for num in range(0, len(x_list1)):
  m = 0
  while m == 0:
    theta1 = 2.0*pi*random()#角度θ(2pi単位)をランダムにするため，random()を使って[0,1]の一様乱数を発生させる。
    theta2 = 2.0*pi*random()
    x_list1[num] += cos(theta1)*cos(theta2)# x方向への移動。cos(θ)
    y_list1[num] += sin(theta1)*cos(theta2)# y方向への移動。sin(θ)
    z_list1[num] += sin(theta2)
    if (x_list1[num])**2+(y_list1[num])**2+(z_list1[num])**2<=(a/4)**2:#金属板に触れたイオンを析出
      x_list2.append(x_list1[num])
      y_list2.append(y_list1[num])
      z_list2.append(z_list1[num])
      square+=1
      print("sq")
      m = 1
    elif (x_list1[num])**2+(y_list1[num])**2+(z_list1[num])**2>=(a*2)**2:#離れていったイオンを排除
      disappeared+=1
      print("dis")
      m = 1
    elif len(x_list2)<=0 :
      m = 0
    else:
      if min(x_list2)-1<=x_list1[num] and x_list1[num]<=max(x_list2)+1 and min(y_list2)-1<=y_list1[num] and y_list1[num]<=max(y_list2)+1 and min(z_list2)-1<=z_list1[num] and z_list1[num]<=max(z_list2)+1:
        for cx in x_list2:
          if (x_list1[num]-cx)**2+(y_list1[num]-y_list2[x_list2.index(cx)])**2+(z_list1[num]-z_list2[x_list2.index(cx)])**2<=1:#新たに析出したスズに触れたイオンを析出
            x_list2.append(x_list1[num])
            y_list2.append(y_list1[num])
            z_list2.append(z_list1[num])
            circle+=1
            print("circ")
            m = 1
            break
        
print(x_list2)
print(y_list2)
print(z_list2)
print("------------------------------------------------")
print("time:"+str(time.time()-t))
print("square:"+str(square))
print("disappeared:"+str(disappeared))
print("circle:"+str(circle))
# for plot
fig = plt.figure(figsize=(5,5))#出力サイズ
ax = Axes3D(fig)#グラフのサイズ
ax.scatter(x_list2,y_list2,z_list2)# (x,y)の散布図
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = (a/4) * np.outer(np.cos(u), np.sin(v))
y = (a/4)  * np.outer(np.sin(u), np.sin(v))
z = (a/4)  * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,color="lightgreen",rcount=100, ccount=100, antialiased=False)
plt.savefig("3d_ball.jpg",dpi=120)
plt.show()