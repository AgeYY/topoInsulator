# Zeyuan Ye, Feb 15, 2020

# Test hoti.py

import __init__
import src.topo.hoti as ht
import numpy as np
from matplotlib import pyplot as plt

########## Test the eigenvalues when delta = 0 ##########
nx, ny = 10, 10 # 10 * 10 sites
kx, ky = np.pi, np.pi
gammaDmambda, delta = 1, 0.0
gammaMesh = np.linspace(-1.2, 1.2, 40)

htHam = ht.hoti(nx, ny)
ham = htHam.ham(kx, ky, gammaDmambda, delta) # Hamiltonian for a specific k
print(ham)
eVal = np.linalg.eigvals(ham) # Find its eigenvalues
eValAna = np.sqrt( 2 + 2 * gammaDmambda**2 + 2 * gammaDmambda * (np.cos(kx) + np.cos(ky)) )
print(eVal, eValAna)



eVal = []
for gammaDmambda in gammaMesh:
    htHam.genEigen(gammaDmambda, delta)
    eVal.append(np.sort(htHam.listEigenVal())) # Obtain the eigenvalues with different gammaDmambda
eVal = np.array(eVal).T

plt.figure(0)

for eValRow in eVal:
    plt.plot(gammaMesh, eValRow, c='b')

plt.show()
