#!/usr/bin/python
import sys
import numpy as np 
from numpy.random import seed
from numpy import pi, sin , cos
from scipy.spatial import Delaunay
from circumradius3d import get_circumradius
import operator

# random seed
seed(1292405)

# number of vertices
Nv = int(sys.argv[1])

# radius of polygon
r = float(sys.argv[2])

# allocate vertices
coords = np.zeros((Nv,3))

# pick random points on sphere
for i in range(0,Nv):

	theta = np.random.uniform(0,2*pi)
	phi = np.random.uniform(0,pi)

	x = r * cos(theta) * sin(phi)
	y = r * sin(theta) * sin(phi)
	z = r * cos(phi)

	coords[i,:] = x,y,z

x = coords[:,0]
y = coords[:,1]
z = coords[:,2]

# triangulate
tt = Delaunay(coords)

# remove triangles that are too big
ntetrahedrons = len(tt.simplices)
triangles = []

# add triangles with radius < maxCR
for i in range(0,ntetrahedrons):
	Ax = x[tt.simplices[i,0]]
	Ay = y[tt.simplices[i,0]]         
	Az = z[tt.simplices[i,0]]
	Bx = x[tt.simplices[i,1]]
	By = y[tt.simplices[i,1]]
	Bz = z[tt.simplices[i,1]]
	Cx = x[tt.simplices[i,2]]
	Cy = y[tt.simplices[i,2]]
	Cz = z[tt.simplices[i,2]]
	Dx = x[tt.simplices[i,3]]
	Dy = y[tt.simplices[i,3]]
	Dz = z[tt.simplices[i,3]]

	# Triangle 1 = ABC = [0,1,2]
	i1 = tt.simplices[i,0]
	i2 = tt.simplices[i,1]
	i3 = tt.simplices[i,2]
	triangles.append((i1,i2,i3))

	# Triangle 2 = ABD  = [0,1,3]
	i1 = tt.simplices[i,0]
	i2 = tt.simplices[i,1]
	i3 = tt.simplices[i,3]
	triangles.append((i1,i2,i3))

	# Triangle 3 = ACD = [0,2,3]
	i1 = tt.simplices[i,0]
	i2 = tt.simplices[i,2]
	i3 = tt.simplices[i,3]
	triangles.append((i1,i2,i3))

	# Triangle 4 = BCD = [1,2,3]
	i1 = tt.simplices[i,1]
	i2 = tt.simplices[i,2]
	i3 = tt.simplices[i,3]
	triangles.append((i1,i2,i3))



# get all triangles on the surface 

# find all triangles involved in one tetrahedron
# i.e. find all unique triangles 
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
for key,value in counts.iteritems():
	if value == 1:
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
		ff.write("%d\t%d\t%d\n"%(i1,i2,i3))

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


