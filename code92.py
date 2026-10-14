import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6 * np.pi, 1000)

y = 3 * np.sin(x) + 1.5 * np.sin(3 * x) + 2 * np.sin(0.5 * x)

maior_y = y[0]
x_do_maior_y = x[0]


for i in range(len(y)):
    y_atual = y[i]
    x_atual = x[i]

    if y_atual > maior_y:
        maior_y = y_atual
        x_do_maior_y = x_atual

print(f"O maior valor no eixo Y é: {maior_y:.2f}")
print(f"Ele ocorre na posição X: {x_do_maior_y:.2f}")


plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Senoide Composta', color='b')


plt.plot(x_do_maior_y, maior_y, 'ro', markersize=8, label=f'Pico Máximo (Y={maior_y:.2f})')
plt.annotate(f'Máximo encontrado:\nY={maior_y:.2f}',
             xy=(x_do_maior_y, maior_y),
             xytext=(x_do_maior_y, maior_y + 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('Busca de Pico Máximo usando Laço de Repetição')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()