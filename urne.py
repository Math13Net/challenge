import random
import numpy as np


def easy(n=3):
    # méthode 1
    urne = []
    for i in range(n):
        for k in range(1, 10):
            urne += [10 * i + k]
    return np.array([urne[0], len(urne)])

def normal(n=3):
    # méthode 2
    urne = []
    for i in range(n):
        for k in range(1, 11):
            urne += [10 * i + k]
        urne.pop(0)
    return np.array([urne[0], len(urne)])


def wtf(n=3):
    # méthode 3
    urne = []
    for i in range(n):
        for k in range(1, 11):
            urne += [10 * i + k]
        urne.pop(random.randrange(len(urne)))
    return np.array([urne[0], len(urne)])


def test(nb_essai=10, nb_etape=100):
  # presentation
  print("012345678901234567890123456789012345678901234567890")
  print("     meth_1         |       meth_2          |        meth_3")
  # essai
  m_1, m_2, m_3 = np.array([0, 0]), np.array([0, 0]), np.array([0, 0])
  for i in range(nb_essai):
    m_1 = easy(nb_etape)
    m_2 = normal(nb_etape)
    m_3 = wtf(nb_etape)
    print(f"low:{m_1[0]:<4.1f} len:{m_1[1]:<6.0f} | low:{m_2[0]:<4.1f} len:{m_2[1]:<6.0f} | low:{m_3[0]:<4.1f} len:{m_3[1]:<6.0f}")

test(nb_essai=5, nb_etape=50000)


