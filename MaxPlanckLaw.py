import matplotlib.pyplot as plt
import numpy as np

# Helvetica LaTeX fonts
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]
})

# Variables
h = 6.626e-34
c = 2.99e+8
k = 1.381e-23
wavelenght = np.arange(1e-7, 1.3e-6, 1e-9)
temp = np.linspace(6000, 9000, 2999)

# Planck Law
def planck_law(longueur_onde, T):
    a = (8*np.pi*h*c)/(longueur_onde**5)
    b = (h*c)/(longueur_onde*k*T)
    P = a/(np.exp(b) - 1.0)
    return P

wavelenght, temp = np.meshgrid(wavelenght, temp)

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

surf = ax.plot_surface(wavelenght*1e9, temp, planck_law(wavelenght, temp), cmap='cividis', antialiased=True) # cividis, hot, CMRmap, GnBu_r, bone

ax.set_xlabel(r'$\lambda$ (nm)')
ax.set_ylabel('T (K)')
ax.set_zlabel(r'$\rho (\lambda, T)$')

cbar = fig.colorbar(surf, shrink=0.5)

plt.subplots_adjust(left=0.2)

# plt.savefig('render.pdf') # To save the fig

plt.show()