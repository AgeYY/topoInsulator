from sympy.physics.paulialgebra import Pauli
import sympy as sym
import numpy as np

#np.array(Pauli(1)).astype(np.complex)
p1 = sym.N(Pauli(1))
print(p1)
