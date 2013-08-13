from math import sqrt
from math import acos
from math import pi
from math import sin
from math import cos
def giveUserDefBC(iX, iY, iZ, iDofNum):
# Apply the analytical solution of a cracked plate subject to mode I loading.

# Material and loading parameters
	k1 = 1.0 # Stress intensity factor
	E = 1.0e4 # Youngs modulus
	nu = 0.3 # Poissons ratio
	mu = E/(2.0*(1.0+nu)) # Shear modulus
	kappa = (3.0-nu)/(1.0+nu) # Plane stress

	# Coordinates of crack tip
	xTip = [1.0, 1.0]

	presVal = 0.0

	t = [1.0, 0.0]

	n = [0.0, 1.0]

	xN = [iX, iY]
	q = [xN[0] - xTip[0],xN[1] - xTip[1]]
	l = sqrt(q[0]*q[0]+q[1]*q[1])
	q[0] = q[0]/l
	q[1] = q[1]/l	

	# Compute polar coordinates
	r = l
	theta = 0.0
	if (q[0]*n[0] + q[1]*n[1]) > 0.0:
		theta =  acos( q[0]*t[0] + q[1]*t[1] );
	else:
		theta = -acos( q[0]*t[0] + q[1]*t[1] );


	if iDofNum == 1:
		# x-direction
		presVal = (k1/(2.0*mu))*sqrt(r/(2.0*pi))*cos(0.5*theta)*( kappa - 1.0 + 2.0*sin(0.5*theta)*sin(0.5*theta) )
	elif  iDofNum == 2:
		# y-direction
		presVal = (k1/(2.0*mu))*sqrt(r/(2.0*pi))*sin(0.5*theta)*( kappa + 1.0 - 2.0*cos(0.5*theta)*cos(0.5*theta) )
	else:
		print 'Warning: no rule for dof number: ', iDofNum

#	print 'presVal: ',presVal
	return presVal
