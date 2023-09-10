#packages
import numpy as np



#spatial constants
dx = 0.5
dy = dx
#M, N represents total non boundary nodes 
U = 4 #x
V = 4 #y

#FTCS for 2D Heat Eqn

#converts matrix to vector [mv] -->row major
#row,col refers to current row,col of element of interest
# U --> max x, V--> max y
mv = lambda row,col: (row - 1)* V + col 

"""
for 3x3 matrix , row = 3  , col = 3
starts at bottom left corner

[ (3,1) (3,2) (3,3); (2,1) (2,2) (2,3); (1,1) (1,2) (1,3)]

(1,1) --> ml = 1
(2,2) --> ml = 5
"""

#initial field:
Q0 = lambda x,y: 3.5*x^2 + 3 *(y -0.5)^2

#BC
"""
dirichlet BCs. 
left = 1, 
right =2, 
top = 3, 
bot =4 
corners = average of adjacent sides
"""


t_steps = 2
A = np.zeros((t_steps,U*V))


#crank nicolson solution for heat equation:
#spatial approximation: centred difference
#temporal approximation: crank nicolson

def check_if_bound(point):
    if U in point: #right bound
        pass
    
    if V in point: #bot bound
        pass

    if 1 in point: #left or top bound
        pass



def calcMolecule(point) -> np.array:
    # point  = row, col refering to position in the matrix/spatial domain
    point = point
    top = point + point[0,1]
    bot = point - point[0,1]
    left = point + point[1,0]
    right = point - point[0,1]
    return 


for t in range(t_steps):
    t = t + 1
    for row in range(len(U)):
        for col in range(len(V)):
            row = row + 1
            col += 1
            a = np.zeros(U*V)

            row_index = mv(row,col)
            col_index = t

            #top:
            top = [row,col + 1] 

            bot = point - point[0,1]
            left = point + point[1,0]
            right = point - point[0,1]


            if col == 1: #left bc
                pass
            if col == U: #right bc
                pass
            if row == 1: #top bc
                pass
            if col == V: #bot bc
                pass
            
            
            












            


            