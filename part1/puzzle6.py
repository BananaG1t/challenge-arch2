import turtle

# The RGB values needed to complete the image are as follows, gained with a HEX colour picker

a = 10
b = 255
c = 135

t = turtle.Turtle()
turtle.colormode(b)
t.fillcolor((a,b,c))
t.pencolor("red")

t.begin_fill()
for i in range(a):
    t.forward(b%c)
    t.left(c)
t.end_fill()


turtle.done()

print(a*b*c)