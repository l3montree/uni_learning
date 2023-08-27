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

