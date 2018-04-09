#!usr/bin/python
from numpy import sqrt
from numpy.random import *

def get_distance(Ax,Ay,Bx,By):
	return sqrt((Ax-Bx)**2 + (Ay-By)**2)




Ax,Ay,Az = rand(2)
Bx,By,Bz = rand(2)

d = get_distance(Ax,Ay,Az,Bx,By,Bz)


