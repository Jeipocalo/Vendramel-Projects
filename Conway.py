import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tamanho da grade
N = 100
M = 100

# Crie uma grade inicial aleatória
grid = np.random.choice([0, 1], N * M, p=[0.8, 0.2]).reshape(N, M)

# Crie uma figura
fig, ax = plt.subplots()

# Função para calcular o próximo estado da grade
def proxima_geracao(*args):
    global grid
    nova_grid = grid.copy()
    for i in range(N):
        for j in range(M):
            vizinhos = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1), (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            total_vivos = sum(grid[x % N, y % M] for x, y in vizinhos)
            if grid[i, j] == 1:
                if total_vivos < 2 or total_vivos > 3:
                    nova_grid[i, j] = 0
            else:
                if total_vivos == 3:
                    nova_grid[i, j] = 1
    grid = nova_grid
    im.set_array(grid)
    return im,

# Plote a grade inicial
im = ax.imshow(grid, cmap='gray')

# Crie a animação
ani = animation.FuncAnimation(fig, proxima_geracao, blit=True, interval=200)

# Mostre a animação
plt.show()
