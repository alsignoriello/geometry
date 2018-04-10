#!usr/bin/python
from numpy import sqrt
from numpy.random import rand

def get_distance(Ax,Ay,Bx,By):
	return sqrt((Ax-Bx)**2 + (Ay-By)**2)


# generate two random points
Ax,Ay = rand(2)
Bx,By = rand(2)

# get distance between points
d = get_distance(Ax,Ay,Bx,By)
print d


