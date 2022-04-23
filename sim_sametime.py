import numpy as np
from random import random,randint
import matplotlib.pyplot as plt
from math import *
import time
from mpl_toolkits.mplot3d.axes3d import Axes3D

a = 20
N = 100
v2_list = []
sq = 0
cir = 0
t = time.time()

def position():
  v1_list = []
  while len(v1_list) != N:
    v1 = np.array([randint(-a,a), randint(-a,a), randint(-a,a)])
    if  (a/4)**2 <= np.linalg.norm(v1) <= a**2:
      v1_list.append(v1)
  return v1_list

def moving(v1_list):
  square = 0
  circle = 0
  v2_list = []
  v3_list = []
  for num in v1_list:
    m = 0
    _ = 0
    while m == 0:
      theta1 = 2.0*pi*random()
      theta2 = 2.0*pi*random()
      backup = num
      ev = np.array([cos(theta1)*cos(theta2), sin(theta1)*cos(theta2), sin(theta2)])
      num = num + ev
      if np.linalg.norm(num) <= (a/4)**2:
        v2_list.append(num)
        square += 1
        m = 1
      elif np.linalg.norm(num) >= (a*2)**2:
        num = backup
        m = 0
      elif len(v2_list)<=0 :
        m = 0
      else:
        for cx in v2_list:
          if np.linalg.norm(num - cx) <= 1:
            v2_list.append(num)
            v3_list.append(num[0])
            circle += 1
            m = 1
            break
    _ += 1
    if _ % 100 == 0:
      print (_)
  return v3_list, square, circle

def info(v_list, square, circle):        
  print(v_list)
  print("------------------------------------------------")
  print("time:"+str(time.time()-t))
  print("square:"+str(square))
  print("circle:"+str(circle))

def graph(v_list):
  x_list = []
  y_list = []
  z_list = []
  for num in v_list:
    x_list.append(v_list[0])
    y_list.append(v_list[1])
    z_list.append(v_list[3])
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

v1_list = position()

v3_list, sq, cir = moving(v1_list)

info(v3_list, sq, cir)

graph(v3_list)