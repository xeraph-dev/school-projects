import math as m
import turtle as t

max_depth = 12
angle = 2 * m.pi / 11
ratio = 0.75

t.delay(0)
t.speed("fastest")
t.hideturtle()

v = t.Turtle()
v.speed("fastest")
v.hideturtle()
v.radians()
v.left(m.pi / 2)
v.teleport(0, -t.screensize()[1])


def tree(
    vs: list[t.Turtle],
    depth: int = 1,
    size: float = 150,
    pensize: int = 10,
):
    nvs: list[t.Turtle] = []

    for v in vs:
        v.pensize(pensize)
        v.forward(size)

        lt = v.clone()
        rt = v.clone()

        lt.left(angle / 2)
        rt.right(angle / 2)

        nvs.append(lt)
        nvs.append(rt)

    if depth == max_depth:
        return

    depth += 1
    size = size * ratio
    pensize = round(pensize * ratio)

    vs = nvs
    tree(vs, depth, size, pensize)


tree([v])


t.mainloop()
