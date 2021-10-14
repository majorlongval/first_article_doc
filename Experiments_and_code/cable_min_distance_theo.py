
# Importing libs
from sympy import *
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Defining symbols
r_1, r_2, D, H_1 = symbols('r_1 r_2 D H_1')

#Defining useful functions
def norm(v:Matrix):
    return sqrt(v[0,0]**2+v[1,0]**2+v[2,0]**2)
def cross_prod(v1:Matrix, v2:Matrix):
    return Matrix(3,1,[v1[1,0]*v2[2,0]-v1[2,0]*v2[1,0],
                       v1[0,0]*v2[2,0]-v1[2,0]*v2[0,0],
                       v1[0,0]*v2[1,0]-v1[1,0]*v2[0,0]])
def dot_prod(v1:Matrix, v2:Matrix):
    return v1[0,0]*v2[0,0]+v1[1,0]*v2[1,0]+v1[2,0]*v2[2,0]

# Developing the math
phi = asin((r_1+r_2)/D)
p1 = Matrix(3,1,[r_1*cos(phi), -r_1*sin(phi),H_1*phi/(2*pi)])
p2 = Matrix(3,1,[-r_1*cos(phi), -r_1*sin(phi),H_1*(3*pi-phi)/(2*pi)])
rho_1 = sqrt(H_1**2+4*pi**2*r_1**2)/(2*pi)
q1 = Matrix(3,1,[-r_1*sin(phi), -r_1*cos(phi),H_1/(2*pi)])
q2 = Matrix(3,1,[r_1*sin(3*pi-phi), r_1*cos(3*pi-phi),-H_1/(2*pi)])
u1 = simplify(q1/rho_1)
u2 = simplify(q2/rho_1)
Lf = 1#rho_1*sqrt(D**2-(r_2+r_1)**2)/r_1
full = simplify((Lf**2)*dot_prod(cross_prod(u1,u2),p2-p1)/norm(cross_prod(u1,u2)))

print_latex(full)
# Turning the full expression into a python function
f = lambdify([r_1, r_2, D, H_1], full)


@np.vectorize
def return_distance(r1, r2, D, H1):
    return f(r1, r2, D, H1)

# Creating values for plotting
res = 0.01
r1 = 1
r2 = 2
dim_indx = r1 + r2
D = np.arange(dim_indx+res, 1.2*dim_indx, res)
H1 = np.arange(res, 0.2*dim_indx, res)
D, H1 = np.meshgrid(D, H1)

val = return_distance(r1, r2, D, H1)

# Drawing the plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(D/dim_indx, H1/dim_indx, val/r1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()
