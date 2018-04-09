#!/usr/bin/python
import sys
import numpy as np
from numpy import sqrt

def get_perim(vertices):
	p = 0
	N = vertices.shape[0]
	for i in range(0,N):
		x1 = vertices[i,0]
		y1 = vertices[i,1]
		if i + 1 < N:
			x2 = vertices[i+1,0]
			y2 = vertices[i+1,1]
		else:
			x2 = vertices[0,0]
			y2 = vertices[0,1]
		p += sqrt((x1-x2)**2+(y1-y2)**2)
	return p

# vertex file
file = sys.argv[1]

# read in 2D polygon
vertices = np.loadtxt(file)

# compute perimeter
p = get_perim(vertices)
print p