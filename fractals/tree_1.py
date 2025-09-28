import math as m
import turtle as t

max_depth = 10
angle = 2 * m.pi / 11
ratio = 0.75

t.speed("fastest")
t.delay(0)
t.hideturtle()

v = t.Turtle()
v.radians()
v.hideturtle()
v.speed("fastest")
v.left(m.pi / 2)
v.teleport(0, -t.screensize()[1])


def tree(
    v: t.Turtle,
    depth: int = 1,
    size: float = 150,
    pensize: int = 10,
):
    v.pensize(pensize)
    v.forward(size)

    if depth == max_depth:
        return

    depth += 1
    size = size * ratio
    pensize = round(pensize * ratio)

    lt = v.clone()
    rt = v.clone()

    lt.left(angle / 2)
    rt.right(angle / 2)

    tree(lt, depth, size, pensize)
    tree(rt, depth, size, pensize)


tree(v)


t.mainloop()
