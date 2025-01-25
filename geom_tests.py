# Tinkering with regular polygons
import numpy as np
import matplotlib.pyplot as plt
import ipdb


N = 3		# number of sides on regular polygon
R = 1.0			# radius of encompassing circle
tau = 0.0			# rotation angle (deg)
dTheta = 1.0		# resolution in theta (deg)



# Compute first segment
psi = 180. * (N - 2) / N 			# internal angle of the regular polygon
alpha = np.deg2rad(psi / 2)						# bisected internal angle, angle between adjacent and hypotenuse in triangle of interest
nu = 360 / N 						# angle span of each of N segments 
theta = np.deg2rad(np.arange(0, nu, dTheta))	# vector of angles, polar coordinate independent variable
rho_poly = R * np.tan(alpha) / (np.sin(theta) + \
		 np.tan(alpha) * np.cos(theta))
rho_circ = R * np.ones(theta.shape)


theta_all = theta
rho_poly_all = rho_poly
for ii in range(N - 1):
	theta_prime = theta + np.deg2rad(nu) * (ii + 1)
	theta_all = np.append(theta_all, theta_prime)
	rho_poly_all = np.append(rho_poly_all, rho_poly)
theta_all = np.append(theta_all, 2 * np.pi)
rho_poly_all = np.append(rho_poly_all, rho_poly_all[0])

# Plot 
plt.figure(2)
plt.polar(theta_all, np.ones(theta_all.shape), color='black', linewidth=2.5)
plt.polar(theta_all, rho_poly_all, color='blue', linewidth=2.5)



# Show plots
plt.show()

# Enter debug
ipdb.set_trace()
