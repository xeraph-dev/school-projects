"""
Draw a regular polygon via the Schläfli symbol
Resources
- https://en.wikipedia.org/wiki/Schläfli_symbol
"""

import turtle as t
import math as m


while (sides := t.numinput("Enter p", "Enter p", minval=3)) is None:
    pass

while (skips := t.numinput("Enter q", "Enter q", minval=1, maxval=sides // 2)) is None:
    pass

t.delay(0)
t.speed("fastest")

screensize = t.screensize()

sides, skips = round(sides), round(skips)
radius = min(screensize[0], screensize[1]) * 0.8

p = sides // m.gcd(sides, skips)
q = skips // m.gcd(sides, skips)

rotation = 45 if sides == 4 else 90

points = [
    t.Vec2D(radius * m.cos(m.radians(angle)), radius * m.sin(m.radians(angle)))
    for angle in [
        (angle * k + rotation) % 360
        for k, angle in enumerate([360 / sides] * sides, start=1)
    ]
] * q


[
    t.goto(point) if point_i > 0 else t.teleport(point[0], point[1])
    for point_i, point in [
        (point_i, points[(point_i + figure_i) % len(points)])
        for figure_i in range(skips // q)
        for point_i in range(len(points) + q)
        if (point_i % skips) == 0
    ]
]


t.mainloop()
