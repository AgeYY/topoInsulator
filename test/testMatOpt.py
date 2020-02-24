# testMatOpt.py
# Zeyuan Ye Feb. 24, 2020

# test matOpt.py
import __init__
import src.cmPrep.tightHam as th
import numpy as np
from matplotlib import pyplot as plt

nLat = 20
hopStre = 1
dim = 1

ham = th.simpleTightMat(nLat, hopStre, dim = dim)
#print(ham) # Print ham and check it
eVal = np.linalg.eigvals(ham)
eVal = np.sort(eVal)

plt.figure(0)
plt.plot(np.arange(nLat), eVal)
plt.show()
