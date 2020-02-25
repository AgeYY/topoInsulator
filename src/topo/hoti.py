# hoti.py
# Zeyuan Ye, Feb 25

# Repeat the works of Fig 2A,B,C,D in wladimir2017 (_wlad17_)
import numpy as np
import src.tool.physics as phy

class hoti():
    '''
    The hamiltonian of equation (6) in _wlad17_. a = lambda = 1 in equation (6)
    capGamma(list): capital gammare in wlad17
    kx, ky(double[]): meshed points of 2 Pi / N * n
    eigen(dic): eigen = {(kx, ky): [eigenVals, eigenVec]}. Eigen values and eigenvector of the system corresponds to a particular set of kx, ky. For this is a four band system, eigenVals = [e0, e1, e2, e3] and eigenvector is a four rows matrix with each row corresponds to each eigenVal.
    '''
    capGamma = [0] * 5 # See def
    kxMesh, kyMesh = np.zeros(0), np.zeros(0) # See def
    eigen = {}

    def __init__(self, nx, ny):
        self.setSites(nx, ny)

    def setSites(self, nx, ny): # Generate the k mesh according the the number of sites. The lattice constant a is 1. Thus kx, ky is meshed into 2 Pi / N * n, where N is the # of lattice sites in one direction, n is integer.
        self.kxMesh = np.arange(nx) * 2 * np.pi / nx
        self.kyMesh = np.arange(nx) * 2 * np.pi / nx

    def genGamma(self):
        # capital gamma in equation (6)
        self.capGamma[0] = np.kron(phy.pauli(3), phy.pauli(0))
        for k in range(1, 4):
            self.capGamma[k] = np.kron(-phy.pauli(2), phy.pauli(k))
        self.capGamma[4] = np.kron(phy.pauli(1), phy.pauli(0))

    def ham(self, kx, ky, gammaDmambda, delta):
        '''
        The hamiltonian of equation (6) in _wlad17_
        gamma, mambda, delta(double): see equation (6)
        '''
        self.genGamma() # Generate capital gamma matrices
        ham = (gammaDmambda + np.cos(kx)) * self.capGamma[4] + np.sin(kx) * self.capGamma[3] + (gammaDmambda + np.cos(ky)) * self.capGamma[2] + np.sin(ky) * self.capGamma[1] + delta * self.capGamma[0]
        return ham

    def genEigen(self, gammaDmambda, delta):
        # Find the eigenvalues and eigenVectors of the system
        for kx in self.kxMesh:
            for ky in self.kyMesh:
                hamMat = self.ham(kx, ky, gammaDmambda, delta)
                self.eigen[(kx, ky)] = np.linalg.eigvals(hamMat)
                #eigen[(kx, ky)][1] = # eigenVectors are not considered now.

    def listEigenVal(self):
        # List all eigenvalues
        eVal = []
        for key in self.eigen:
             eVal.extend(list(self.eigen[key].real)) # The imagnary part should be very small since ham is hermitian
        return eVal
