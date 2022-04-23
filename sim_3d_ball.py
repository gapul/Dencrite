import numpy as np
from random import random,randint
import matplotlib.pyplot as plt
from math import *
import time
from mpl_toolkits.mplot3d.axes3d import Axes3D
import os

d = 2
a = 20
N = 100
t = time.time()

def position_2d_sq():
  x_list = []
  y_list = []
  while len(y_list) != N:
    x = randint(-a,a)#イオンの開始位置を定義
    y = randint(-a,a)
    if abs(x+y)+abs(x-y) >= a/2+0.5 and x**2+y**2 <= a**2:
      x_list.append(x)
      y_list.append(y)
  return x_list, y_list

def position_3d():
  x_list = []
  y_list = []
  z_list = []
  while len(z_list) != N:
    x = randint(-a,a)#イオンの開始位置を定義
    y = randint(-a,a)
    z = randint(-a,a)
    if  (a/4)**2 <= x**2+y**2+z**2 <= a**2:
      x_list.append(x)
      y_list.append(y)
      z_list.append(z)
  return x_list, y_list, z_list

def moving_2d():
  m = 0
  x_list1, y_list1 = position_2d_sq()
  x_list2 = []
  y_list2 = []
  square = 0
  circle = 0
  while len(y_list2) != len(y_list1):
    num = 0
    while num != len(y_list1):
      if x_list1[num] == 0:
        pass
      else:
        print("a")
        theta = 2.0*pi*random()
        x_backup = x_list1[num]
        y_backup = y_list1[num]
        x_list1[num] += cos(theta)
        y_list1[num] += sin(theta)
        if abs(x_list1[num]+y_list1[num])+abs(x_list1[num]-y_list1[num])<=a/2+0.5:
          x_list2.append(x_list1[num])
          y_list2.append(y_list1[num])
          x_list1[num] = 0
          y_list1[num] = 0
          m += 1
          square += 1
        elif (x_list1[num])**2+(y_list1[num])**2 >= (a*2)**2:#離れていったイオンをreturn
          x_list1[num] = x_backup
          y_list1[num] = y_backup
        elif len(x_list2)<=0 :
          pass
        else:
          if min(x_list2)-1<=x_list1[num] and x_list1[num]<=max(x_list2)+1 and min(y_list2)-1<=y_list1[num] and y_list1[num]<=max(y_list2)+1 :
            for cx in x_list2:
              if (x_list1[num]-cx)**2+(y_list1[num]-y_list2[x_list2.index(cx)])**2 <= 1:
                x_list2.append(x_list1[num])
                y_list2.append(y_list1[num])
                x_list1[num] = 0
                y_list1[num] = 0
                m += 1
                circle += 1
                print(str(len(y_list2)) + '/' + str(len(y_list1)))
      num += 1

  return x_list2, y_list2, square, circle

def moving_3d():
  x_list1, y_list1, z_list1 = position_3d()
  x_list2 = []
  y_list2 = []
  z_list2 = []
  square = 0
  circle = 0
  for num in range(0, len(z_list1)):
    m = 0
    while m == 0:
      theta1 = 2.0*pi*random()#角度θ(2pi単位)をランダムにするため，random()を使って[0,1]の一様乱数を発生させる。
      theta2 = 2.0*pi*random()
      x_backup = x_list1[num]
      y_backup = y_list1[num]
      z_backup = z_list1[num]
      x_list1[num] += cos(theta1)*cos(theta2)# x方向への移動。cos(θ)
      y_list1[num] += sin(theta1)*cos(theta2)# y方向への移動。sin(θ)
      z_list1[num] += sin(theta2)
      if (x_list1[num])**2+(y_list1[num])**2+(z_list1[num])**2<=(a/4)**2:#金属板に触れたイオンを析出
        x_list2.append(x_list1[num])
        y_list2.append(y_list1[num])
        z_list2.append(z_list1[num])
        square += 1
        m = 1
        print("0")
      elif (x_list1[num])**2+(y_list1[num])**2+(z_list1[num])**2>=(a*2)**2:#離れていったイオンを排除
        x_list1[num] = x_backup
        y_list1[num] = y_backup
        z_list1[num] = z_backup
        m = 0
        print("1")
      elif len(x_list2)<=0 :
        m = 0
        print("2")
      else:
        if min(x_list2)-1<=x_list1[num] and x_list1[num]<=max(x_list2)+1 and min(y_list2)-1<=y_list1[num] and y_list1[num]<=max(y_list2)+1 and min(z_list2)-1<=z_list1[num] and z_list1[num]<=max(z_list2)+1:
          for cx in x_list2:
            if (x_list1[num]-cx)**2+(y_list1[num]-y_list2[x_list2.index(cx)])**2+(z_list1[num]-z_list2[x_list2.index(cx)])**2<=1:#新たに析出したスズに触れたイオンを析出
              x_list2.append(x_list1[num])
              y_list2.append(y_list1[num])
              z_list2.append(z_list1[num])
              circle += 1
              m = 1
              print("3")
              break
    if num % 100 == 0:
      print (num)
  return x_list2, y_list2, z_list2, square, circle

def info_2d(x_list, y_list, square, circle):
  print(x_list)
  print(y_list)
  print("------------------------------------------------")
  print("time:"+str(time.time()-t))
  print("square:"+str(square))
  print("circle:"+str(circle))

def info_3d(x_list, y_list, z_list, square, circle):
  print(x_list)
  print(y_list)
  print(z_list)
  print("------------------------------------------------")
  print("time:"+str(time.time()-t))
  print("square:"+str(square))
  print("circle:"+str(circle))

def graph_2d_ball(x_list, y_list):
  fig = plt.figure(figsize=(5,5))#出力サイズ
  ax = fig.add_subplot(1,1,1)#グラフのサイズ
  plt.scatter(x_list,y_list)# (x,y)の散布図
  rec=plt.Rectangle(xy=(-a/4,-a/4), width=a/2, height=a/2,fill=False)#四角形の定義
  ax.add_patch(rec)#四角形の描写の追加
  plt.xlabel('X') # x軸のラベル
  plt.ylabel('Y') # y軸のラベル
  plt.xlim([-a,a]) # x軸の範囲
  plt.ylim([-a,a])#y軸の範囲
  plt.show()

def graph_3d_ball(x_list, y_list, z_list):
  fig = plt.figure(figsize=(5,5))#出力サイズ
  ax = Axes3D(fig)#グラフのサイズ
  ax.scatter(x_list,y_list,z_list)# (x,y)の散布図
  u = np.linspace(0, 2 * np.pi, 100)
  v = np.linspace(0, np.pi, 100)
  x = (a/4) * np.outer(np.cos(u), np.sin(v))
  y = (a/4)  * np.outer(np.sin(u), np.sin(v))
  z = (a/4)  * np.outer(np.ones(np.size(u)), np.cos(v))
  ax.plot_surface(x, y, z,color="lightgreen",rcount=100, ccount=100, antialiased=False)
  for num in range(0, len(x_list)):
    x=[x_list[num]]
    y=[y_list[num]]
    z=[z_list[num]]
    for px in range(0, len(x_list)):
      if (x_list[num]-x_list[px])**2+(y_list[num]-y_list[px])**2+(z_list[num]-z_list[px])**2<=1 and (x_list[num]-x_list[px])**2+(y_list[num]-y_list[px])**2+(z_list[num]-z_list[px])**2 != 0:
        x.append(x_list[px])
        y.append(y_list[px])
        z.append(z_list[px])
        ax.plot(x, y, z, marker="o", color="#00aa00", ms=4, mew=0.5)
  plt.savefig("3d_ball.jpg",dpi=120)
  plt.show()

if d == 2:
  x_list, y_list, square, circle = moving_2d()
  info_2d(x_list, y_list, square, circle)
  graph_2d_ball(x_list, y_list)

else:
  x_list, y_list, z_list, square, circle = moving_3d()
  info_3d(x_list, y_list, z_list, square, circle)
  graph_3d_ball(x_list, y_list, z_list)