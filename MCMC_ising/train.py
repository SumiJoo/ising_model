from environment import Ising_model
import numpy as np
import math
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
temperature=0.01
mode='u'
size=100
num_episode=600000
lattice=Ising_model(temperature, size,mode)
energy_s=[]
for i in range(int(num_episode/10)):
    energy=0
    for j in range(10):
        
        N=np.random.randint(low=0,high=size)
        M=np.random.randint(low=0,high=size)
        if lattice.energy(N,M)<0:
            lattice.state[N][M]*=-1
        elif math.exp(-lattice.energy(N,M)/temperature)>np.random.random():
            lattice.state[N][M]*=-1
        energy+=lattice.tol_energy()[0]
    energy_s.append(energy/10)

plt.plot(list(range(len(energy_s))),energy_s)
plt.xlabel('episodes')
plt.ylabel('total_energy')
plt.savefig('episode_.pdf')
lattice_=np.zeros((size,size))
'''for i in range(size):
    for j in range(size):
        lattice_[i][j]=lattice.state[i][j]'''
plt.imshow(lattice.state, cmap='gray', origin='upper')  # 灰度图，黑白表示自旋
plt.colorbar(label="Spin Value")  # 添加色条
plt.title("Ising Model Spin Configuration")
plt.savefig('lattice.pdf')