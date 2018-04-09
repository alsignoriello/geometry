#!/usr/bin/python
import sys
import numpy as np 

# # http://stackoverflow.com/questions/1165647/how-to-determine-if-a-list-of-polygon-points-are-in-clockwise-order
def checkCounterClockwise(vertices):
	# check if counter-clockwise
	sumEdges = 0
	N = vertices.shape[0]

	for i in range(0,N):
		# current vertex
		x1 = vertices[i,0]
		y1 = vertices[i,1]

		# next vertex
		if i + 1 < N:
			x2 = vertices[i+1,0]
			y2 = vertices[i+1,1]
		else:
			x2 = vertices[0,0]
			y2 = vertices[0,1]

		sumEdges += float(x2 - x1) / float(y2 + y1)

	if sumEdges > 0:
		return True
	else:
		return False


# vertex file
file = sys.argv[1]

# read in 2D polygon
vertices = np.loadtxt(file)

# compute area
cc = checkCounterClockwise(vertices)
print cc

# reverse vertices
vertices = np.flip(vertices,axis=0)
cc = checkCounterClockwise(vertices)
print cc


