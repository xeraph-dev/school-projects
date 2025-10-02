import random

import matplotlib.pyplot as plt
import numpy as np

CELL_COUNT = 1000
MAX_GENERATIONS = 100


class Cell:
    y: int
    x: int
    alive: bool
    was_alive: bool

    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
        self.alive = False
        self.was_alive = False
        self.random()

    def kill(self):
        data[self.y, self.x] = 0

    def revive(self):
        data[self.y, self.x] = 1

    def random(self):
        self.alive = random.randint(0, 1) == 1
        self.update_status()

    def update(self):
        alive = sum(
            1
            for y in range(self.y - 1, self.y + 2)
            for x in range(self.x - 1, self.x + 2)
            if 0 <= y < CELL_COUNT
            and 0 <= x < CELL_COUNT
            and y != self.y
            and x != self.x
            and cells[y * CELL_COUNT + x].was_alive
        )
        if self.alive:
            self.alive = 2 <= alive <= 3
        else:
            self.alive = alive == 3

    def update_status(self):
        if self.alive:
            self.revive()
        else:
            self.kill()

        self.was_alive = self.alive


data = np.zeros_like(np.add.outer(range(CELL_COUNT), range(CELL_COUNT)))
cells = [Cell(y, x) for y, _ in enumerate(data) for x, _ in enumerate(data[y])]

fig, ax = plt.subplots()

for gen in range(MAX_GENERATIONS):
    ax.clear()
    ax.axis("off")
    axes = ax.imshow(data, cmap="binary")

    for cell in cells:
        cell.update()

    for cell in cells:
        cell.update_status()

    plt.pause(0.5)

plt.show()
