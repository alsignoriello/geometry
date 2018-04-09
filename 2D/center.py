#!/usr/bin/python
import sys
import numpy as np 

# compute area for vertices
# vertices = (N,2) with (x,y)
def get_center(vertices):
	N = vertices.shape[0]
	sumx = 0.
	sumy = 0.
	for i in range(0,N):
		sumx += vertices[i,0]
		sumy += vertices[i,1]
	cx = sumx / N
	cy = sumy / N

	return cx,cy


# vertex file
file = sys.argv[1]

# read in 2D polygon
vertices = np.loadtxt(file)

# compute area
cx,cy = get_center(vertices)
print cx,cy