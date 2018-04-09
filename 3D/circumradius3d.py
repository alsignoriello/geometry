import numpy as np
from numpy.linalg import det


def getCircumradius(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz, Dx, Dy, Dz):
	# a
	a = np.zeros((4,4))
	a[0,:] = [Ax, Ay, Az, 1.]
	a[1,:] = [Bx, By, Bz, 1.]
	a[2,:] = [Cx, Cy, Cz, 1.]
	a[3,:] = [Dx, Dy, Dz, 1.]
	
	D_a = det(a)
	
	# Determinant of X
	Detx = np.zeros((4,4))
	Detx[0,:] = [Ax**2 + Ay**2 + Az**2, Ay, Az, 1.]
	Detx[1,:] = [Bx**2 + By**2 + Bz**2, By, Bz, 1.]
	Detx[2,:] = [Cx**2 + Cy**2 + Cz**2, Cy, Cz, 1.]
	Detx[3,:] = [Dx**2 + Dy**2 + Dz**2, Dy, Dz, 1.]
	
	D_x = det(Detx)
	
	# Determinant of Y
	Dety = np.zeros((4,4))
	Dety[0,:] = [Ax**2 + Ay**2 + Az**2, Ax, Az, 1.]
	Dety[1,:] = [Bx**2 + By**2 + Bz**2, Bx, Bz, 1.]
	Dety[2,:] = [Cx**2 + Cy**2 + Cz**2, Cx, Cz, 1.]
	Dety[3,:] = [Dx**2 + Dy**2 + Dz**2, Dx, Dz, 1.]
	Dety = - Dety
	
	D_y = det(Dety)
	
	# Determinant of Z
	Detz = np.zeros((4,4))
	Detz[0,:] = [Ax**2 + Ay**2 + Az**2, Ax, Ay, 1.]
	Detz[1,:] = [Bx**2 + By**2 + Bz**2, Bx, By, 1.]
	Detz[2,:] = [Cx**2 + Cy**2 + Cz**2, Cx, Cy, 1.]
	Detz[3,:] = [Dx**2 + Dy**2 + Dz**2, Dx, Dy, 1.]
	
	D_z = det(Detz)
	
	# c
	c = np.zeros((4,4))
	c[0,:] = [Ax**2 + Ay**2 + Az**2, Ax, Ay, Az] 
	c[1,:] = [Bx**2 + By**2 + Bz**2, Bx, By, Bz]
	c[2,:] = [Cx**2 + Cy**2 + Cz**2, Cx, Cy, Cz]
	c[3,:] = [Dx**2 + Dy**2 + Dz**2, Dx, Dy, Dz]
	
	D_c = det(c)
	
	# circumcenter
	x0 = D_x / (2. * D_a)
	y0 = D_y / (2. * D_a)
	z0 = D_z / (2. * D_a)
	# print x0,y0,z0
	# return x0, y0, z0
	
	
	# # circumradius
	r = ((D_x**2 + D_y**2 + D_z**2 - 4. * D_a * D_c)**(0.5)) / (2. * abs(D_a))
	# # print r
	return r



# Ax = 1.  	
# Ay = 1.  	
# Az = 1.  	
# Bx = 1.  	
# By = -1.  	
# Bz = -1.  	
# Cx = -1.  	
# Cy = 1.  	
# Cz = -1.  	
# Dx = -1.  	
# Dy = -1.  	
# Dz = 1  	

# # a
# a = np.zeros((4,4))
# a[0,:] = [Ax, Ay, Az, 1.]
# a[1,:] = [Bx, By, Bz, 1.]
# a[2,:] = [Cx, Cy, Cz, 1.]
# a[3,:] = [Dx, Dy, Dz, 1.]

# D_a = det(a)

# # Determinant of X
# Detx = np.zeros((4,4))
# Detx[0,:] = [Ax**2 + Ay**2 + Az**2, Ay, Az, 1.]
# Detx[1,:] = [Bx**2 + By**2 + Bz**2, By, Bz, 1.]
# Detx[2,:] = [Cx**2 + Cy**2 + Cz**2, Cy, Cz, 1.]
# Detx[3,:] = [Dx**2 + Dy**2 + Dz**2, Dy, Dz, 1.]

# D_x = det(Detx)

# # Determinant of Y
# Dety = np.zeros((4,4))
# Dety[0,:] = [Ax**2 + Ay**2 + Az**2, Ax, Az, 1.]
# Dety[1,:] = [Bx**2 + By**2 + Bz**2, Bx, Bz, 1.]
# Dety[2,:] = [Cx**2 + Cy**2 + Cz**2, Cx, Cz, 1.]
# Dety[3,:] = [Dx**2 + Dy**2 + Dz**2, Dx, Dz, 1.]
# Dety = - Dety

# D_y = det(Dety)

# # Determinant of Z
# Detz = np.zeros((4,4))
# Detz[0,:] = [Ax**2 + Ay**2 + Az**2, Ax, Ay, 1.]
# Detz[1,:] = [Bx**2 + By**2 + Bz**2, Bx, By, 1.]
# Detz[2,:] = [Cx**2 + Cy**2 + Cz**2, Cx, Cy, 1.]
# Detz[3,:] = [Dx**2 + Dy**2 + Dz**2, Dx, Dy, 1.]

# D_z = det(Detz)

# # c
# c = np.zeros((4,4))
# c[0,:] = [Ax**2 + Ay**2 + Az**2, Ax, Ay, Az] 
# c[1,:] = [Bx**2 + By**2 + Bz**2, Bx, By, Bz]
# c[2,:] = [Cx**2 + Cy**2 + Cz**2, Cx, Cy, Cz]
# c[3,:] = [Dx**2 + Dy**2 + Dz**2, Dx, Dy, Dz]

# D_c = det(c)

# # circumcenter
# x0 = D_x / (2. * D_a)
# y0 = D_y / (2. * D_a)
# z0 = D_z / (2. * D_a)
# print x0,y0,z0


# # circumradius
# r = ((D_x**2 + D_y**2 + D_z**2 - 4. * D_a * D_c)**(0.5)) / (2. * abs(D_a))
# print r






