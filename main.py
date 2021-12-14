import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


x = [0, 2000, 4000, 6000, 8000, 10000]
y = [0, 1500, 2200, 2600, 2900, 3100]

plt.xticks(x)


ax.plot(x, y, label="Обычный алгоритм")

ax.scatter(x, y, c='blue')

ax.grid()
ax.set_xlabel('Частота (Гц)')
ax.set_ylabel('Шкала мел')

plt.show()
plt.savefig('1.pdf')