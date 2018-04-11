#!/usr/bin/python
import sys
import numpy as np 

# compute area for vertices
# vertices = (N,2) with (x,y)
def get_area(vertices):
	N = vertices.shape[0]
	cross = 0.
	for i in range(0,N):
		x1,y1 = vertices[i,:]
		if i + 1 < N:
			x2,y2 = vertices[i+1,:]
		else:
			x2,y2 = vertices[0,:]
		cross += ((x1*y2) - (x2*y1))
	# area should be positive
	# can be negative if vertices clockwise
	return abs(0.5*cross)



# vertex file
file = sys.argv[1]

# read in 2D polygon
vertices = np.loadtxt(file)

# compute area
a = get_area(vertices)
print a