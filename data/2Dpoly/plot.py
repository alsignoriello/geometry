#!/usr/bin/python
import sys
import numpy as np 
import matplotlib.pyplot as plt 

# vertex file
file = sys.argv[1]

# read in vertices
vertices = np.loadtxt(file)

# number of vertices
Nv = vertices.shape[0]


for i in range(0,Nv):
	x1,y1 = vertices[i,:]
	x2,y2 = vertices[(i+1)%Nv,:]
	plt.scatter(x1,y1,color="deeppink",alpha=1,marker=".")
	plt.scatter(x2,y2,color="deeppink",alpha=1,marker=".")
	plt.plot([x1,x2],[y1,y2],color="k",alpha=0.5,linewidth=2)

plt.axis('equal')
plt.axis('off')
plt.show()