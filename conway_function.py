# suite conway
# prop 1 : c_n est constiuté de 1, 2 et 3 uniquement
# prop 2 : c_n est constituée de 92 briques élémentaires
# liste ici : http://www.se16.info/js/lands2.htm
# prop 3 : tous les termes de la suite possède 1 nombre pair de chiffre sauf le terme initial
# prop 4 : à partir du 4ème terme, les termes de rang pair se terminent par 211, ceux de rang imparis par 221
# prop 5 : à partir du 8ème terme, les termes commencent cycliquement par 1113, 3113 et 1321
# prop 6 : c_n est croissante et l_n aussi
# prop 7 : les termes de la suite possède 50pc de 1, 31pc de 2 et 19pc de 3

#import numpy as np
#import matplotlib.pyplot as plt
# from scipy import stats
import pandas as pd
from itertools import groupby

# construction de la suite
def look_and_say(iterations, sequence='1'):
    arr = [sequence]
    def get_sequence(arr,iterations,sequence):
        if iterations == 0:
            return arr
        else:
            current = ''.join(str(len(list(group))) + key for key,group in groupby(sequence))
            arr.append(current)
            get_sequence(arr,iterations-1,current)
        return arr
    
    final_sequence = get_sequence(arr,iterations,sequence)
    return final_sequence

# construction des données complémentaires : longueur des termes, quotient
def complement(conway_sequence):
  x = conway_sequence
  # longueur du terme - quotient
  b = [len(i) for i in x]
  c = [round(b[i+1]/b[i],3) for i in range(len(b)-1)]
  c.append('NaN')
  return b, c

# sauvegarde dans un fichier text
def save_data(x, b, c, file, n):
  file = open(file, 'w')
  file.write(f"terme longueur quotient\n")
  for i in range(n):
    file.write(f"{x[i]} {b[i]} {c[i]}\n")
  file.close()


# construction de la base bdd avec le fichier txt
def conway_bdd(file):
  return pd.read_csv(file, sep = " ")

  
# prop 1 : c_n est constiuté de 1, 2 et 3 uniquement
def prop_1(n, file):
  df = conway_bdd(file)
  resultat = True
  for i in range(n):
    if ("1" or "2" or "3") not in str(df.terme[i]):
      resultat = False
  return resultat 

def prop_2():
  pass

# prop 3 : tous les termes de la suite possède 1 nombre pair de chiffre sauf le terme initial
def prop_3(n, file):
  df = conway_bdd(file)
  resultat = True
  for i in range(1, n):
    if len(str(df.terme[i]))%2 != 0:
      resultat = False
  return resultat

def prop_4():
  pass

def prop_5():
  pass

def prop_6():
  pass

def prop_7():
  pass

if __name__=='__main__':
  pass
