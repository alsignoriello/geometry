#!usr/bin/python
from numpy import sqrt
from numpy.random import *

def get_distance(Ax,Ay,Az,Bx,By,Bz):
	return sqrt((Ax-Bx)**2 + (Ay-By)**2 + (Az-Bz)**2)




Ax,Ay,Az = rand(3)
Bx,By,Bz = rand(3)

d = get_distance(Ax,Ay,Az,Bx,By,Bz)


