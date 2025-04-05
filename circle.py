import turtle as t

t.speed("fastest")
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


t.color('red', 'red')
draw_heart()
t.done()
