import numpy as np
import math
class Ising_model:
    def __init__(self,temperature,size,mode):
        self.size=size
        self.tempe=temperature
        self.state=self.set_state(mode)

    # the initial state
    def set_state(self,mode):
        if mode =='r':
            return np.random.choice([-1,1],(self.size,self.size))
        else:
            return np.ones((self.size,self.size))
    # delta energy caused by flip
    def energy(self,i,j):
        return -2*self.state[i][j]*(self.state[self.bound_con(i-1)][j]+self.state[self.bound_con(i+1)][j]+self.state[i][self.bound_con(j-1)]+self.state[i][self.bound_con(j+1)])

    def tol_energy(self):
        E=0
        e=0
        E2=0
        for i in range (self.size):
            for j in range(self.size) :
                e=self.energy(i,j)
                E+=e
                E2+=math.pow(e,2)
        U=(1/math.pow(self.size,2))*E
        U2=(1/math.pow(self.size,2))*E2
        return U,U2

    def bound_con(self,i):
        if i >=self.size-1:
            return 0
        if i<0:
            return self.size-1
        else:
            return i