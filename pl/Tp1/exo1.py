import numpy as np
import matplotlib.pyplot as plt

# Définir les limites du graphique
x = np.linspace(-10, 10)
y = np.linspace(-10, 10)
X, Y = np.meshgrid(x, y)

Z1 = 6 - X - 2*Y
Z2 = 4 - X - Y
Z3 = 3 -X
Z4 = X
Z5 = Y

# Tracer les contraintes
plt.contourf(X, Y, Z1, levels=[- np.inf, 0], colors=['red'], alpha=0.15)
xa = np.linspace(-10, 10)
xb = (6 - xa) / 2
plt.plot(xa, xb, color='blue', label='x1 + 2x2 <= 6')

plt.contourf(X, Y, Z2, levels=[- np.inf, 0], colors=['red'], alpha=0.15)
xb = 4 - xa
plt.plot(xa, xb, color='red', label='x1 + x2 <= 4')

plt.contourf(X, Y, Z3, levels=[- np.inf, 0], colors=['red'], alpha=0.15)
xa=3
plt.axvline(xa, color='purple', label='x1 <= 3')

plt.contourf(X, Y, Z4, levels=[- np.inf, 0], colors=['red'], alpha=0.15)
xa=0
plt.axvline(xa, color='black', label='x1>=0')

plt.contourf(X, Y, Z5, levels=[- np.inf, 0], colors=['red'], alpha=0.15)
xb=0
plt.axvline(xb,color ='black' ,label='x2>=0')


for Z in [2, 4, 6, 8, 10]:
    y_obj = Z - 2*xa
    plt.plot(xa, y_obj, '--', color='red', label=f'Z={Z}')

# Personnaliser le graphique
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Représentation graphique du système")
plt.legend()

plt.show()
'''
Max Z = 2x1 + x2
x1 + 2x2 <= 6
x1 + x2 <= 4
x1 >= 3
x1 >= 0 , x2 >= 0
'''
