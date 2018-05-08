#!usr/bin/python
import sys
import numpy as np
from numpy import sqrt

# https://stackoverflow.com/questions/26312570/calculate-surface-area-of-a-3d-mesh
def get_surfarea(Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz):
	ax = Bx - Ax
	ay = By - Ay
	az = Bz - Az
	bx = Cx - Ax
	by = Cy - Ay 
	bz = Cz - Az
	cx = ay*bz - az*by
	cy = az*bx - ax*bz
	cz = ax*by - ay*bx
	return 0.5 * sqrt(cx*cx + cy*cy + cz*cz)



# vertex file
vfile = sys.argv[1]

# face file
ffile = sys.argv[2]

# read in triangular mesh 
vertices = np.loadtxt(vfile)
faces = np.loadtxt(ffile)
faces = faces.astype(int)


# compute surface area
Nf = faces.shape[0]
sa = 0
for i in range(0,Nf):
	i1,i2,i3 = faces[i,:]
	Ax,Ay,Az = vertices[i1,:]
	Bx,By,Bz = vertices[i2,:]
	Cx,Cy,Cz = vertices[i3,:]

	sa += get_surfarea(Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz)

# surface area
print sa