#!/usr/bin/python
from numpy import sqrt, arctan2, pi, sin, cos, arccos
from numpy.random import uniform,rand,seed
import numpy as np

''' Angle between 3 points '''
# get angle assuming vertex is p1
# http://stackoverflow.com/questions/1211212/how-to-calculate-an-angle-from-three-points
def get_angle(p1,p2,p3):
	radian = 0
	p12 = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	p13 = sqrt((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2)
	p23 = sqrt((p2[0]-p3[0])**2 + (p2[1]-p3[1])**2)
	if p12 != 0 and p13 != 0:
		try:
			radian = arccos((p12**2 + p13**2 - p23**2)/(2*p12*p13))
		except ValueError:
			print "Domain Error"
			pass
	return radian

# transform vector (x,y) into angle theta
def vector_2_angle(v):
	x = v[0]
	y = v[1]
	theta = arctan2(y,x)
	return theta


# generate random angle theta between -pi - pi
def rand_angle():		
	theta = uniform(-pi,pi)
	return theta


# returns angle unit vector
def angle_2_vector(theta):
	x = cos(theta)
	y = sin(theta)
	
	# transform to unit vector
	v = np.array([x,y])
	uv = unit(v)

	return uv

# get normal vector from 2 vectors
def normal(v1,v2):
	pass

def unit(v):
	d = sqrt(v[0]**2 + v[1]**2)
	v[0] = v[0]/d
	v[1] = v[1]/d
	return v

# random seed
seed(1292405)

# get a random angle
theta = rand_angle()
print theta

# transform to vector
x,y = angle_2_vector(theta)
print x,y

# generate 3 points 
p1 = rand(2)
p2 = rand(2)
p3 = rand(2)

# get angle between 3 points
# first point is vertex
theta = get_angle(p1,p2,p3)
print theta






