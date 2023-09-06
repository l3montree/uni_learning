#packages
import numpy as np

#spatial constants
dx = 0.5
dy = dx
#M, N represents total non boundary nodes 
M = 4 #x
N = 4 #y

#FTCS for 2D Heat Eqn

#converts matrix to row: row major
ml = lambda x,y: (N+2)*y+x

list_ = np.zeros()

t_steps = 5
x_steps =5
y_steps =5


for t in range(t_steps):
    for x in range(x_steps):
        for y in range(y_steps):
            