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
