# testSshHam.py
# Zeyuan Ye Feb. 24, 2020

# test sshHam.py

import __init__
import src.cmPrep.sshHam as sh
import numpy as np
from matplotlib import pyplot as plt

nLat = 40
t = 1
delT = 0.3
hopSIn, hopSOut = t + delT, t - delT

ham = sh.sshModel(nLat, hopSIn, hopSOut)
#print(ham) # Print ham and check it

eVal = np.linalg.eigvals(ham)
eVal = np.sort(eVal)

plt.figure(0)
plt.plot(np.arange(len(eVal)), eVal)
plt.show()
