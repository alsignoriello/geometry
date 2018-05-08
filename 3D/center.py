#!/usr/bin/python
import sys
import numpy as np 


# compute center for vertics
# vertices = (N,2) with (x,y,z)
def get_center(vertices):
	N = vertices.shape[0]
	sumx = 0
	sumy = 0
	sumz = 0
	for i in range(0,N):
		sumx += vertices[i,0]
		sumy += vertices[i,1]
		sumz += vertices[i,2]
	cx = sumx/N
	cy = sumy/N
	cz = sumz/N 

	return cx,cy,cz


# vertex file
file = sys.argv[1]


# load data
vertices = np.loadtxt(file)

# compute center of mass
cx,cy,cz = get_center(vertices)
print cx,cy,cz


