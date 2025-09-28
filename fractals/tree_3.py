import itertools as it
from collections.abc import Generator
from math import e, pi

import matplotlib.pyplot as plt

ratio = 0.95
angle = 2 * pi / 11


def tree() -> Generator[list[complex]]:
    row = [(0 + 0j, 0 + 10j)]
    depth = 1

    yield 0, row
    while True:
        nrow: list[tuple[complex, complex]] = []

        for vec in row:
            lvec = (vec[1] - vec[0]) * ratio**depth * e ** (1j * angle / 2) + vec[1]
            rvec = (vec[1] - vec[0]) * ratio**depth * e ** (-1j * angle / 2) + vec[1]

            nrow.append((vec[1], lvec))
            nrow.append((vec[1], rvec))

        depth, row = depth + 1, nrow
        yield depth, row


for depth, row in it.islice(tree(), 10):
    for vec in row:
        x = [vec[0].real, vec[1].real]
        y = [vec[0].imag, vec[1].imag]
        plt.plot(x, y, color="black")

plt.show()
