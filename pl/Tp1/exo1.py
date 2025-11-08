<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

# Définir la grille
x = np.linspace(0, 10, 400)
y = np.linspace(0, 10, 400)
X, Y = np.meshgrid(x, y)

# Contraintes
Z1 = X + 2*Y - 6      # x1 + 2x2 <= 6
Z2 = X + Y - 4        # x1 + x2 <= 4
Z3 = X - 3            # x1 <= 3

# Zone faisable
feasible = (Z1 <= 0) & (Z2 <= 0) & (Z3 <= 0) & (X >= 0) & (Y >= 0)
plt.contourf(X, Y, feasible, levels=[0.5, 1], colors=['lightblue'], alpha=0.6)

# Tracer les droites de contraintes
xa = np.linspace(0, 10, 200)
plt.plot(xa, (6 - xa)/2, color='blue', linewidth=2, label='x1 + 2x2 = 6')
plt.plot(xa, 4 - xa, color='green', linewidth=2, label='x1 + x2 = 4')
plt.plot(np.full_like(xa, 3), xa, color='orange', linewidth=2, label='x1 = 3')
plt.axvline(0, color='black', linewidth=1, label='x1 = 0')
plt.axhline(0, color='black', linewidth=1, label='x2 = 0')

# Tracer les droites de la fonction objectif : Z = 2x1 + x2
for Z in [2, 4, 6, 8, 10]:
    y_obj = Z - 2*xa
    plt.plot(xa, y_obj, '--', color='red', linewidth=1)

# Personnalisation du graphique
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Zone faisable (toutes contraintes satisfaites)')
plt.legend(loc='upper right', fontsize=8)
plt.grid(True, linestyle='--', alpha=0.4)

plt.show()
=======
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
>>>>>>> 84859807c659802f5fb906ef0c51e814dbe570c0
