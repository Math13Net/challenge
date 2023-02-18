import mpmath as mp
from mpmath import *

import time as t
from time import time

def premier_test():
  mp.dps = 50
  mp.pres = 150
  #print(mp)

  x = mp.mpmathify('1/37')
  print(f"la valeur de 1/37 est : {x}")
  #print(type(x))

  resultat = mp.nstr(x, n=30)                                # converti en string pour slicer
  print(f"la partie qui se répète est : {resultat[2:5]}")
  #print(type(resultat))

#premier_test()

def periodique(p):
  reste = []
  quotient = []
  diviseur = p
  # initialisation
  dividende_en_cours = 1
  quotient_en_cours = 1 // p
  reste_en_cours = 1 % p

  # boucle de recherche
  while(reste_en_cours not in reste):
    #print(f"{dividende_en_cours} = {quotient_en_cours} * {diviseur} + {reste_en_cours}")
    reste.append(reste_en_cours)
    quotient.append(quotient_en_cours)
    dividende_en_cours = reste_en_cours*10
    quotient_en_cours = dividende_en_cours // p
    reste_en_cours = dividende_en_cours % p
    
  reste.append(reste_en_cours)
  quotient.append(quotient_en_cours)
  dividende_en_cours = reste_en_cours*10
  quotient_en_cours = dividende_en_cours // p
  reste_en_cours = dividende_en_cours % p
    
  # affiche le resultat
  a = ""
  for i in range(1, len(quotient)):
    a += str(quotient[i])
  longueur = len(a)
  print(f"la partie périodique de 1/{p} est {a}")
  print(f"cette partie périodique est de longueur {longueur}")
  if longueur == p-1:
    # source : https://www.apmep.fr/IMG/pdf/Sa-03-Germoni-maths_non_appliquees.pdf
    print(f"10 est une racine primitive modulo {p}")

#periodique(17)

# utilisation des mp.mpmathify
def recherche_motif(mot):
  curseur = 0
  motif = mot[curseur]
  entier = len(mot)//len(motif)
  mot_check = mot[:entier*len(motif)]      # tronquer le mot pour le recouvrir de motif
  while motif*int(len(mot)/len(motif)) != mot_check:
    curseur += 1
    motif += mot[curseur]
    entier = len(mot)//len(motif)
    mot_check = mot[:entier*len(motif)]
  return motif

def periode_directe(p):
  mp.dps = 10**5
  mp.pres = 3*10**5
  fraction_str = '1/'+str(p)
  x = mp.mpmathify(fraction_str)         # mpmathinfinity ne fonctionne pas directement
  resultat = mp.nstr(x, n=10**5)             # converti en string pour slicer
  resultat = resultat[2:]                # enlève le 0 et le . dans le string
  motif = recherche_motif(resultat)
  print(f"dans la fraction {fraction_str}, la partie qui se répète est : {motif}")
  print(f"cette partie périodique est de longueur {len(motif)}")
  if len(motif) == p-1:
    print(f"10 est une racine primitive modulo {p}")

def temps(p):
  debut = t.time()
  periodique(p)
  duree = debut - t.time()
  print("temps de calcul : {duree}")


def comparaison(p):
  debut_1 = t.time()
  periodique(p)
  fin_1 = t.time()
  duree_1 = fin_1 - debut_1
  debut_2 = t.time()
  periode_directe(p)
  fin_2 = t.time()
  duree_2 = fin_2 - debut_2
  print(f"algo 1 : {duree_1}")
  print(f"algo 2 : {duree_2}")



comparaison(19463)

#a = "abad"
#b = a*10
#print(recherche_motif(b))