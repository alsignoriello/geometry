#!/usr/bin/python
import numpy as np


''' Line of Best Fit '''
def lineofbestfit(x,y):

	# determine best fit line
	par = np.polyfit(x, y, 1, full=True)
	
	slope=par[0][0]
	intercept=par[0][1]
	# xl = [min(x), max(x)]
	# yl = [slope*xx + intercept for xx in xl]
	
	return slope, intercept



''' Lines Intersect '''
def linesIntersect(line1,line2):

	x1 = [line1[0],line1[2]]
	y1 = [line1[1],line1[3]]
	a, c = lineofbestfit(x1,y1)

	x2 = [line2[0],line2[2]]
	y2 = [line2[1],line2[3]]
	b, d = lineofbestfit(x2,y2)

	x = (d-c) / (a-b)
	y = a * x + c
	if x > max(x1[0],x1[1],x2[0],x2[1]) and x < min(x1[0],x1[1],x2[0],x2[1]):
		if y > max(y1[0],y1[1],y2[0],y2[1]) and y < min(y1[0],y1[1],y2[0],y2[1]):
			return True
	return False
	


''' Slope of a Line '''
def getSlope(x1,y1,x2,y2):
	if x1 - x2 != 0:
		return float((y1-y2) / (x1-x2))
	else:
		return 0