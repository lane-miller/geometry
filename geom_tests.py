# Tinkering with regular polygons
import numpy as np
import matplotlib.pyplot as plt
import ipdb


N = 4		# number of sides on regular polygon
R = 1.0			# radius of encompassing circle
tau = 10.0			# rotation angle (deg)
dTheta = 1.0		# resolution in theta (deg)
center = (-3,-3)



# Compute first segment
psi = 180. * (N - 2) / N 			# internal angle of the regular polygon
alpha = np.deg2rad(psi / 2)						# bisected internal angle, angle between adjacent and hypotenuse in triangle of interest
nu = 360 / N 						# angle span of each of N segments 
theta = np.deg2rad(np.arange(0, nu, dTheta))	# vector of angles, polar coordinate independent variable
rho_poly = R * np.tan(alpha) / (np.sin(theta) + \
		 np.tan(alpha) * np.cos(theta))
rho_circ = R * np.ones(theta.shape)

# Compute remaining points
theta_all = theta
rho_poly_all = rho_poly
for ii in range(N - 1):
	theta_prime = theta + np.deg2rad(nu) * (ii + 1)
	theta_all = np.append(theta_all, theta_prime)
	rho_poly_all = np.append(rho_poly_all, rho_poly)
theta_all = np.append(theta_all, 2 * np.pi)
rho_poly_all = np.append(rho_poly_all, rho_poly_all[0])

# Rotate shape tau degrees
theta_all += np.deg2rad(tau)

# Translate to requested center
x = rho_poly_all * np.cos(theta_all) + center[0]
y = rho_poly_all * np.sin(theta_all) + center[1]

theta_all_prime = np.arctan(y / x)
rho_all_prime = np.sqrt(x**2 + y**2)

# Plot 
# plt.figure(1)
# plt.polar(theta_all, np.ones(theta_all.shape), color='black', linewidth=2.5)
# plt.polar(theta_all, rho_poly_all, color='blue', linewidth=2.5)

# Plot
plt.figure(2)
# plt.polar(theta_all_prime, rho_all_prime, color='black', linewidth=2.5)
plt.plot(x, y, color='black', linewidth=2.5)

# Show plots
plt.show()

# Enter debug
ipdb.set_trace()
