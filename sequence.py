# suite : https://youtu.be/pAMgUB51XZA
import math
import matplotlib.pyplot as plt
import sympy


def sequence_1():
# SEQUENCE ONE : 
# https://oeis.org/A133058
# ------------------------------------------------  
  n = 1000

  x = [0,1]
  y = [1,1]
  for i in range(2,n):
    x.append(i)
    p = math.gcd(i, y[-1])
    if p == 1:
      y.append(y[-1]+i+1)
    else:
      y.append(int(y[-1]/p))
  
  # repérage des valeurs
  #for i in range(n):
  #  print(f"{x[i]:^6d} , {y[i]:^8d}")

  # look for 638
  for i in range(2,n,2):
    if y[i] == 1:
      print(i)
      break
      
  # look for a pattern before 638 ???
  #for mod in range(4,10):
  #  for i in range(int(n/mod)-1):
  #    plt.plot(x[i*mod], y[i*mod], '.', color='blue')
  #    plt.plot(x[i*mod+1], y[i*mod+1], '.', color='green')
  #    plt.plot(x[i*mod+2], y[i*mod+2], '.', color='brown')
  #    plt.plot(x[i*mod+3], y[i*mod+3], '.', color='purple')
  
  #  plt.axis([-100, 1000, 0, 2000])
  #  plt.xlim(-10, 1000)
  #  plt.ylim(-10, 2000)
  #  plt.savefig('sequence'+f'{mod}'+'.png')

def sequence_2():      
# ------------------------------------------------------
# SEQUENCE TWO
# https://oeis.org/A265326  
# ------------------------------------------------
  n = 5000

  x = []
  y = []
  for i in range(1,n):
    x.append(i)
    p = sympy.prime(i)
    y.append( p - int(bin(p)[:1:-1], 2) )  # je ne comprends pas cette ligne
    
  # repérage des valeurs
  #for i in range(n-1):
  #  print(f"{x[i]:^6d} , {y[i]:^8d}")
  
  # plot
  for i in range(int(n)-1):
    plt.plot(x[i], y[i], '.', color='blue')
  
  plt.axis([-100, 1000, 0, 2000])
  plt.xlim(-10, 5000)
  plt.ylim(-10, 10000)
  plt.savefig('sequence'+'.png')


    
  # look for a pattern before 638 ???
  #for mod in range(4,10):
  #  for i in range(int(n/mod)-1):
  #    plt.plot(x[i*mod], y[i*mod], '.', color='blue')
  #    plt.plot(x[i*mod+1], y[i*mod+1], '.', color='green')
  #    plt.plot(x[i*mod+2], y[i*mod+2], '.', color='brown')
  #    plt.plot(x[i*mod+3], y[i*mod+3], '.', color='purple')
  
  #  plt.axis([-100, 1000, 0, 2000])
  #  plt.xlim(-10, 1000)
  #  plt.ylim(-10, 2000)
  #  plt.savefig('sequence'+f'{mod}'+'.png')

sequence_2()