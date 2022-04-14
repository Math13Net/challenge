# fichier de valeurs : https://oeis.org/A265326/b265326.txt 

import matplotlib.pyplot as plt

def para():
  n = 100
  
  x = [i for i in range(n)]
  y = []
  
  f = open("suite.txt", "r")
  ligne = f.readline()

  for j in range(n):            
  #while ligne:    ca serait mieux
    i = 0
    while ligne[i]!=" ":
      i += 1
    nombre_en_texte = ligne[i+1:-1]
    nombre = int(nombre_en_texte)
    y.append(nombre)
    ligne = f.readline()
  f.close()

  # repérage des valeurs
  #for i in range(n-1):
  #  print(f"{x[i]:^6d} , {y[i]:^8d}")


  # tracé de la suite
  for i in range(int()-1):                   #mettre n au lieu de 100
    plt.plot(x[i], y[i], '.', color='blue')
    
 
  plt.xlim(-100, 100)
  plt.ylim(-100, 100)
  plt.savefig('para.png')
