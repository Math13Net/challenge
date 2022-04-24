#import numpy as np
#import matplotlib.pyplot as plt
# from scipy import stats
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
def save_data(x, b, c):
  file = open('text.txt', 'w')
  file.write(f"terme longueur quotient\n")
  for i in range(n):
    file.write(f"{x[i]} {b[i]} {c[i]}\n")
  file.close()
  
  print("nombre de caractères : ", )
  print("quotients : ", )

if __name__=='__main__':
  n = 10
  x = look_and_say(10, sequence='1')
  longueur, quotient = complement(x)
  save_data(x, longueur, quotient)
  