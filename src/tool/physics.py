# physics

import numpy as np
import sys

def pauli(i):
    if(i == 0): return np.array([[1, 0], [0, 1]]).astype(np.complex)
    elif(i == 1): return np.array([[0, 1], [1, 0]]).astype(np.complex)
    elif(i == 2): return np.array([[0, -1j], [1j, 0]])
    elif(i == 3): return np.array([[1, 0], [0, -1]])
    else:
        sys.exit("ERROR: the valid input of pauli is 0, 1, 2 or 3")

