import numpy as np
import matplotlib.pyplot as plt
# Definice funkce pro kvadratický výraz 2x^2 - 8x + 6

# Definice funkce pro kvadratický výraz -x^2 + 5x - 4
def quadratic_function_last(x):
    return -x**2 + 5*x - 4

# Rozsah x hodnot
x_values_last = np.linspace(-1, 6, 400)

# Vypočítáme y hodnoty pro kvadratickou funkci
y_values_last = quadratic_function_last(x_values_last)

# Vytvoření grafu
plt.figure(figsize=(8, 6))
plt.plot(x_values_last, y_values_last, label=r"$-x^2 + 5x - 4$", color='teal')

# Kořeny paraboly (kde funkce = 0)
roots_last = [1, 4]  # Kořeny z předchozího výpočtu
plt.scatter(roots_last, [0, 0], color='red', zorder=5, label="Roots")

# Osy
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

# Zobrazíme oblast, kde je funkce menší nebo rovna 0
plt.fill_between(x_values_last, y_values_last, where=(y_values_last <= 0), color='lightcyan', label=r"$-x^2 + 5x - 4 \leq 0$")

# Ostatní nastavení grafu
plt.title(r"Graf $-x^2 + 5x - 4 \leq 0$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Zobrazení grafu
plt.grid(True)
plt.show()

