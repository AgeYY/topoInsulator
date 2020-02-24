# matOpt.py
# Zeyuan Ye, Feb. 23, 2020

# Matrix operation

import sys
import numpy as np

def simpleTightMat(nLat, hopStre, dim = 1):
    '''
    Generate the hamiltonian for tight binding model in one and two dimension, with periodic boundary condiction. Ref: Your OneNote and [Altland_A.,_Simons_B.D.]_Condensed_Matter_Field_T
    nLat(int): number of latice sites alone one dimenstion
    hopStre(double): hopping strength, i.e. t in Altland's text book
    dim(int): dimension of your lattice, either 1 or 2.
    '''
    ham = np.zeros((nLat, nLat)) # hamiltonian
    for i in range(nLat):
        for j in range(nLat):
            if(abs(i - j) == 1): # nearest site in the middle
                ham[i, j] = -hopStre
            elif((i == 0 and j == nLat - 1) or (j == 0 and i == nLat - 1)): # the two bounds
                ham[i, j] = -hopStre
    if(dim == 1):
        return ham
    elif(dim == 2):
        ham2 = np.kron(ham, np.identity(nLat)) + np.kron(np.identity(nLat), ham)
        return ham2
    else:
        sys.exit("ERROR: the valid dimension is 1 or 2")

