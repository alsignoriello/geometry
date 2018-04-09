#!/usr/bin/python
import sys
import numpy as np 
from numpy import sqrt,arccos,pi


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

# There are 2 ways of doing this...

# http://stackoverflow.com/questions/16625507/python-checking-if-point-is-inside-a-polygon
def point_in_poly(x,y,vertices):
	xi = []
	yi = []
	N = vertices.shape[0]
	for i in range(0,N):
		xi.append(vertices[i,0])
		yi.append(vertices[i,1])

	poly = zip(xi,yi)

	n = len(poly)
	inside = False

	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xints:
						inside = not inside
		p1x,p1y = p2x,p2y

	return inside

# sum the angles from point to vertices
# if the sum == 2*pi, it is inside (including machine precision)
# else: outside the polygon
def inside_poly(x,y,vertices):
	sumVectors = 0
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
		p1 = (x,y)
		p2 = (x1,y1)
		p3 = (x2,y2)
		angle = get_angle(p1,p2,p3)
		sumVectors += angle

	# if sumVectors == 2pi, inside
	inside = False
	if abs(sumVectors - 2*pi) < 10**-14: 
		inside = True
	print sumVectors

	return inside


# vertex file
file = sys.argv[1]

# read in 2D polygon
vertices = np.loadtxt(file)

# pick point inside polygon
x1 = 10
y1 = 10

# pick point outside polygon
x2 = 20
y2 = 2

print point_in_poly(x1,y1,vertices)
print point_in_poly(x2,y2,vertices)
print inside_poly(x1,y1,vertices)
print inside_poly(x2,y2,vertices)





