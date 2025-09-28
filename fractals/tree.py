import itertools as it
from math import e, pi

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

size_ratio = 0.95
linewidth_ratio = 0.75
angle = 2 * pi / 11
base_linewidth = 8
max_depth = 10
samples = 10


def tree():
    row = [(0 + 0j, 0 + 10j)]
    depth = 1

    yield row
    while True:
        nrow: list[tuple[complex, complex]] = []

        for vec in row:
            dvec = (vec[1] - vec[0]) * size_ratio**depth
            lvec = dvec * e ** (1j * angle / 2) + vec[1]
            rvec = dvec * e ** (-1j * angle / 2) + vec[1]

            nrow.append((vec[1], lvec))
            nrow.append((vec[1], rvec))

        row = nrow
        yield nrow
        depth += 1


fig, ax = plt.subplots()

all_artists: list[list[plt.Line2D]] = []


def animate(data):
    artists: list[plt.Line2D] = []

    depth = 0

    for vecs in data:
        depth = vecs[0]
        x = [vecs[1][0], vecs[1][1]]
        y = [vecs[2][0], vecs[2][1]]
        linewidth = base_linewidth * linewidth_ratio**depth

        line = plt.plot(x, y, color="green", linewidth=linewidth)
        artists.append(line)

    last_artists = all_artists[
        abs(len(all_artists) - (samples - 1)) : abs(len(all_artists) - (samples - 2))
    ]
    for lines in it.chain.from_iterable(last_artists):
        for line in lines:
            line.set_color("black")

    all_artists.append(artists)

    return artists


frames = it.chain.from_iterable(
    zip(
        *(
            zip(
                it.repeat(lvl[0], samples - 1),
                it.pairwise(np.linspace(vec[0].real, vec[1].real, num=samples)),
                it.pairwise(np.linspace(vec[0].imag, vec[1].imag, num=samples)),
            )
            for vec in lvl[1]
        )
    )
    for lvl in enumerate(it.islice(tree(), max_depth))
)


ani = animation.FuncAnimation(
    fig,
    func=animate,
    init_func=lambda: [],
    frames=frames,
    interval=50,
    cache_frame_data=False,
    repeat=False,
)
plt.axis("off")
ani.save("tree.gif")
# plt.show()
