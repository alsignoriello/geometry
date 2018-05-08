#!/usr/bin/pyton
import sys
import numpy as np 
from numpy import sin,cos,sqrt,pi
from numpy.random import seed

# random seed
seed(1292405)

# Number of vertices
Nv = int(sys.argv[1])

# radius of polygon
r = float(sys.argv[2])

# center of polygon
cx = 10.
cy = 10.

# allocate array for vertices
vertices = np.zeros((Nv,2))

for i in range(0,Nv):

	# pick vertices at random intervals on circle
	lb = i * 2 * pi / Nv
	ub = (i+1) * 2 * pi / Nv
	theta = np.random.uniform(lb,ub)

	# pick vertices evenly spaced
	# theta = (i * 2 * pi)/Nv

	x = cx + r*cos(theta)/(sqrt(cos(theta)**2 + sin(theta)**2))
	y = cy + r*sin(theta)/(sqrt(cos(theta)**2 + sin(theta)**2))

	vertices[i,:] = x,y

np.savetxt("vertices.txt",vertices)