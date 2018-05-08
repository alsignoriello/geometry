#!/usr/bin/python
from numpy.random import rand, seed
from numpy import sqrt, arccos

# p1 is vertex
def get_angle(p1,p2,p3):
	radian = 0
	p12 = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
	p13 = sqrt((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2 + (p1[2]-p3[2])**2)
	p23 = sqrt((p2[0]-p3[0])**2 + (p2[1]-p3[1])**2 + (p2[2]-p3[2])**2)
	if p12 != 0 and p13 != 0:
		try:
			radian = arccos((p12**2 + p13**2 - p23**2)/(2*p12*p13))
		except ValueError:
			print "Domain Error"
			pass
	return radian



# random seed
seed(1292405)

# generate 3 points 
p1 = rand(3)
p2 = rand(3)
p3 = rand(3)

# get angle between 3 points
# first point is vertex
theta = get_angle(p1,p2,p3)
print theta






