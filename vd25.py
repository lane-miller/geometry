import numpy as np
from matplotlib.patches import Rectangle, Circle
import matplotlib.pyplot as plt
import ipdb
from img_pixelate import downsample_image

# Inputs
x = 1
d = 0.1
nrow = 20
ncol = 30
img_path = "vd25img.png"

# Get image data
img_data = np.flipud(downsample_image(img_path, (nrow, ncol)))
R = img_data[:,:,0].flatten()
G = img_data[:,:,1].flatten()
B = img_data[:,:,2].flatten()

# Initial Calcs
p = 2 * (d + 17 * x / 10)
q = p / (1 + np.sqrt(2))
l = p * (2 + np.sqrt(2)) / (1 + np.sqrt(2))
quad = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
Rbase = [((5 * (q + d) + 7 * x) / 10, d / 2, x, x),
         ((5 * (q + d) + 2 * x) / 10 + x / 2, (d + 2 * x) / 2, x, x / 5),
         ((q + d + x) / 2, d / 2, x / 5, x)]
Cbase = [((5 * (q + d) + 12 * x) / 10, (5 * d + 12 * x) / 10, x / 2),
         ((5 * (q + d) + 7 * x) / 10 - x / 5, (d + x) / 2, x / 2)]
xg, yg = np.meshgrid(np.arange(ncol), np.arange(nrow))
xg = xg.flatten()
yg = yg.flatten()
# plt.figure()
# plt.plot(xg,yg, 'ko')
# plt.show()
# ipdb.set_trace()

shapes = []
for xb, yb, r, g, b in zip(xg, yg, R, G, B):
	for ii in range(len(quad)):
		qx = quad[ii][0]
		qy = quad[ii][1]
		shapes.append(Circle((xb * l, yb * l), x / 2**0.5, facecolor=(r, g, b)))
		cb = l / 2
		shapes.append(Circle((xb * l + cb, yb * l + cb), x / 2**0.5, facecolor=(r, g, b)))
		for jj1 in range(len(Rbase)):
			shapes.append(Rectangle((Rbase[jj1][0] * qx + xb * l, 
									Rbase[jj1][1] * qy + yb * l), 
									Rbase[jj1][2] * qx, 
									Rbase[jj1][3] * qy,
									facecolor=(r, g, b)))
									#  edgecolor='black',
									#  alpha=0.4))
		for jj1 in range(len(Rbase)):
			shapes.append(Rectangle((Rbase[jj1][1] * qx + xb * l, 
									Rbase[jj1][0] * qy + yb * l), 
									Rbase[jj1][3] * qx, 
									Rbase[jj1][2] * qy,
									facecolor=(r, g, b)))
									#  edgecolor='black',
									#  alpha=0.4))
		for kk1 in range(len(Cbase)):
			shapes.append(Circle((Cbase[kk1][0] * qx + xb * l, 
								Cbase[kk1][1] * qy + yb * l), 
								Cbase[kk1][2],
								facecolor=(r, g, b)))
								#edgecolor='black',
								#alpha=0.4))
		for kk1 in range(len(Cbase)):
			shapes.append(Circle((Cbase[kk1][1] * qx + xb * l, 
								Cbase[kk1][0] * qy + yb * l), 
								Cbase[kk1][2],
								facecolor=(r, g, b)))
								#edgecolor='black',
								#alpha=0.4))
print(f"total shapes: {len(shapes)}")
# plot
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_patch(shape)
ax.set_aspect("equal")
plt.xlim([-3, ncol * 5])
plt.ylim([-3, nrow * 5])
plt.axis('off')
plt.show()
        
 