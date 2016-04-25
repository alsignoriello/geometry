#!/usr/bin/python


# There are 2 ways of doing this right now...
# http://stackoverflow.com/questions/16625507/python-checking-if-point-is-inside-a-polygon
def point_in_poly(x,y,vertices):
	xi = []
	yi = []
	for i in range(0,len(vertices),2):
		xi.append(vertices[i])
		yi.append(vertices[i+1])

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
def insidePoly(x,y,vertices):
	sumVectors = 0
	for i in range(0,len(vertices),2):
		x1 = vertices[i]
		y1 = vertices[i+1]
		if i + 2 >= len(vertices):
			x2 = vertices[0]
			y2 = vertices[1]
		else:
			x2 = vertices[i+2]
			y2 = vertices[i+3]
		p1 = (x,y)
		p2 = (x1,y1)
		p3 = (x2,y2)
		angle = getAngle(p1,p2,p3)
		sumVectors += angle

	# if sumVectors == 2pi, inside
	if sumVectors >= 6.28: 
		# print x,y,sumVectors,vertices
		return True

	return False

