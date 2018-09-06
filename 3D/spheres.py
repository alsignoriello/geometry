#!/usr/bin/python
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from numpy import sqrt


cx = 10
cy = 10
cz = 10

xw = 0.5
yw = 0.5
zw = 0.5



# make grid
X,Y,Z = np.mgrid[0:20:xw,0:20:yw,0:20:zw]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = 5
# fill in points with inside or outside sphere
sphere = np.zeros_like(X)
print sphere.shape
for i in range(0,X.shape[0]):
	for j in range(0,X.shape[1]):
		for k in range(0,X.shape[2]):
			x = X[i,j,k]
			y = Y[i,j,k]
			z = Z[i,j,k]

			d = sqrt((x-cx)**2+(y-cy)**2+(z-cz)**2)
			if d < r:
				sphere[i,j,k] = 1
				ax.scatter(x,y,z,color="k")


plt.show()



# # save as image
# # write z stacks to file
# for i in range(0,sphere.shape[2]):
# 	print i
# 	np.savetxt("/Users/Lexi/Documents/geometry/data/spheres/%.2f/%d.txt"%(xw,i),sphere[:,:,i])











