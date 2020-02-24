# sshHam.py
# Zeyuan Ye, Feb 24, 2020

# SSH model in _P85, topological insulator, shun-qing shen_

import sys
import numpy as np

def sshModel(nLat, hopSIn, hopSOut):
    '''
    Generate the hamiltonian for one dimensional SSH model, with periodic boundary condiction. Ref: Your OneNote and shun-qing shen, topological insulator
    nLat(int): number of latice sites alone one dimenstion
    hopSIn(double): hopping strength inside an unit cell
    hopSOut(double): hopping strength inter unit cells
    '''
    hamI = np.identity(nLat) # hamiltonian about the interaction inside one unit cell
    interI = np.array([[0, hopSIn], [hopSIn, 0]]) # interaction between (1A, 1B) and (1B, 1A)
    hamI = np.kron(hamI, interI)
    hamL = np.zeros((nLat, nLat)) # hamiltonian from the left to the right cell, which is also the upper triangular of the total hamiltonian. Since hamiltonian is hermitian, you could do the hermitian conjugate the generate the lower triangular hermitian (also hamR).
    for i in range(nLat):
        for j in range(nLat):
            if(j - i == 1): # nearest site in the middle
                hamL[i, j] = 1
            elif(j == 0 and i == nLat - 1): # the right boundary
                hamL[i, j] = 1
    interL = np.array([[0, 0], [hopSOut, 0]]) # Hamiltonian from the left to right unit cell, as you could see, only (1B, 2A) has non-zero value.
    hamL = np.kron(hamL, interL)
    hamR = hamL.T # The hopping strength is real here, so hermitian is indeed just transposition.
    return hamL + hamR + hamI # total hamiltonian
