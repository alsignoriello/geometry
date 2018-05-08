#!/usr/bin/python
import numpy as np
from mayavi.mlab import *

# load coordinates and faces
verts = np.loadtxt("vertices.txt")
faces = np.loadtxt("faces.txt")

x = verts[:,0]
y = verts[:,1]
z = verts[:,2]

# plot mesh of cell
figure(size = (400,400),bgcolor = (0,0,0))
mesh = triangular_mesh(x, y, z, faces,opacity=1,representation='surface',color=(0.2, 0.9, 0.2))
mesh = triangular_mesh(x, y, z, faces,opacity=0.5,line_width=0.2,representation='wireframe',color=(0, 0, 0))

# shading properties
mesh.actor.property.interpolation = 'phong'
mesh.actor.property.specular = 0.1
mesh.actor.property.specular_power = 100

show()