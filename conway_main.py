#import numpy as np
#import matplotlib.pyplot as plt
# from scipy import stats
import conway_function as cv


  
 
if __name__=='__main__':
  n = 10
  x = cv.look_and_say(10, sequence='1')
  file = "text.txt"
  
  longueur, quotient = cv.complement(x)
  cv.save_data(x, longueur, quotient, file, n)
  
  bdd = cv.conway_bdd(file)
  
  print(cv.prop_3(n, file))


