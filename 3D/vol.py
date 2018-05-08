#!usr/bin/python
import sys
import numpy as np 

# https://stackoverflow.com/questions/1406029/how-to-calculate-the-volume-of-a-3d-mesh-object-the-surface-of-which-is-made-up
def get_volume(Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz):
	v321 = Cx*By*Az
	v231 = Bx*Cy*Az
	v312 = Cx*Ay*Bz
	v132 = Ax*Cy*Bz
	v213 = Bx*Ay*Cz
	v123 = Ax*By*Cz
	return (1./6.)*(-v321 + v231 + v312 - v132 - v213 + v123)


# vertex file
vfile = sys.argv[1]

# face file
ffile = sys.argv[2]


# read in triangular mesh 
vertices = np.loadtxt(vfile)
faces = np.loadtxt(ffile)
faces = faces.astype(int)


# compute volume
Nf = faces.shape[0]
vol = 0
for i in range(0,Nf):
	i1,i2,i3 = faces[i,:]
	Ax,Ay,Az = vertices[i1,:]
	Bx,By,Bz = vertices[i2,:]
	Cx,Cy,Cz = vertices[i3,:]

	vol += get_volume(Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz)

# sign of volume depends on ordering of triangles
print abs(vol)
