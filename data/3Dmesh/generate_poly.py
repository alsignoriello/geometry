#!/usr/bin/python
import sys
import numpy as np 
from numpy.random import seed
from numpy import pi, sin , cos
from scipy.spatial import Delaunay
import operator

# random seed
seed(1292405)

# number of vertices
# Nv = int(sys.argv[1])
N = 10

# radius of polygon
r = float(sys.argv[1])

# allocate vertices
coords = []

# move to center
cx = 10
cy = 10
cz = 10


# pick random points on sphere
for i in range(0,N):
	theta = (i * 2 * pi)/N
	for j in range(0,N+1):
		phi = (j*pi)/N
		print theta, phi

	# theta = np.random.uniform(0,2*pi)
	# phi = np.random.uniform(0,pi)

		x = cx + r * cos(theta) * sin(phi)
		y = cy + r * sin(theta) * sin(phi)
		z = cz + r * cos(phi)
		# print x,y,z
		
		if (x,y,z) not in coords:
			coords.append((x,y,z))

coords = np.array(coords)
x = coords[:,0]
y = coords[:,1]
z = coords[:,2]

# triangulate
tt = Delaunay(coords)
ntetrahedrons = len(tt.simplices)
triangles = []

for i in range(0,ntetrahedrons):
	i1 = tt.simplices[i,0]
	i2 = tt.simplices[i,1]
	i3 = tt.simplices[i,2]
	i4 = tt.simplices[i,3]
	triangles.append((i1,i2,i3))
	triangles.append((i2,i3,i4))
	triangles.append((i1,i3,i4))
	triangles.append((i1,i2,i4))


# get all triangles on the surface 
# i.e. find all triangles involved in one tetrahedron
counts = {}
for i1,i2,i3 in triangles:

	# order 3 min -> max
	i_sort = np.sort([i1,i2,i3])
	tri = (i_sort[0],i_sort[1],i_sort[2])

	if tri in counts:
		counts[tri] += 1
	else:
		counts[tri] = 1

vertices = {}
f = open("triangles.txt","w")
ff = open("faces.txt","w")
vcount = 0
dists = []
A = np.zeros(3)
B = np.zeros(3)
C = np.zeros(3)
CC = np.array([cx,cy,cz])
for key,value in counts.iteritems():
	if value == 1:
		i1 = key[0]
		i2 = key[1]
		i3 = key[2]
		Ax = x[key[0]]
		Ay = y[key[0]]
		Az = z[key[0]]
		Bx = x[key[1]]
		By = y[key[1]]
		Bz = z[key[1]]
		Cx = x[key[2]]
		Cy = y[key[2]]
		Cz = z[key[2]]
		f.write("%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\n"%
				(Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz))
		if (Ax,Ay,Az) in vertices:
			i1 = vertices[(Ax,Ay,Az)]
		else:
			i1 = vcount
			vertices[(Ax,Ay,Az)] = i1
			vcount += 1
		if (Bx,By,Bz) in vertices:
			i2 = vertices[(Bx,By,Bz)]
		else:
			i2 = vcount
			vertices[(Bx,By,Bz)] = i2
			vcount += 1
		if (Cx,Cy,Cz) in vertices:
			i3 = vertices[(Cx,Cy,Cz)]
		else:
			i3 = vcount
			vertices[(Cx,Cy,Cz)] = i3
			vcount += 1

		# check vertex order
		A[:] = Ax,Ay,Az
		B[:] = Bx,By,Bz
		C[:] = Cx,Cy,Cz
		N = np.cross((B - A),(C - A))
		w = np.dot(N,A-CC)
		
		if w < 0:
			ff.write("%d\t%d\t%d\n"%(i1,i2,i3))
		else:
			ff.write("%d\t%d\t%d\n"%(i3,i2,i1))
f.close()
ff.close()

fv = open("vertices.txt","w")
sorted_v = sorted(vertices.items(), key=operator.itemgetter(1))
for key,value in sorted_v:
	x = key[0]
	y = key[1]
	z = key[2]
	fv.write("%f\t%f\t%f\n"%(x,y,z))
fv.close()


