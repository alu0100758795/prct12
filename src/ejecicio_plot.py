# practica plot

import sys, random
from math import *
import matplotlib.pyplot as plt
import numpy as np

u=['1.e-10', '1.e-50', '1.e-100', '1.e-150', '1.e-200']
u1=range(5)

def f(a):
  b=0.2
  return eval(expr1)

def g(a):
  b=0.2
  return eval(expr2)

if __name__=='__main__':

  fichero=open('resultado.txt', 'r')
  
  for i in range(1,15):
    
    expr1=fichero.readline()
    expr2=fichero.readline()

    error=[fichero.readline(), fichero.readline(), fichero.readline(), fichero.readline(), fichero.readline()]
    
    a = np.linspace(0, 1, 10)  
    y = np.zeros(len(a))       
    t = np.zeros(len(a))
    
    for i in xrange(len(a)):
      y[i] = f(a[i])
    for i in xrange(len(a)):
      t[i] = g(a[i])
    
    diagrama1 = plt.figure(1)

    plt.subplot(211)
    plt.plot(a,y, 'r')
    plt.plot(a,t, 'bp')
    
    plt.subplot(212)
    plt.plot(u1,error,'bo')
    
    plt.xticks(range(len(u)),u)
    
    plt.savefig('imagen'+str(i)+'.png')

  fichero.close()
