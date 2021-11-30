from turtle import *  # imports turtle

# since we have to draw such squares over and over again, we can use a function


def draw_square():
    i = 0
    while i < 4:
        forward(30)
        right(90)
        i += 1


# draw squares in loop


# upper part of the figure
for i in range(1, 5):
    for j in range(i):
        draw_square()
        forward(30)

    backward(i * 30)
    right(90)
    forward(30)
    left(90)


# bottom part of the figure
for i in range(5, 0, -1):
    for j in range(i):
        draw_square()
        forward(30)

    backward(i * 30)
    right(90)
    forward(30)
    left(90)

# the purpose of this line is to keep
# the picture / window on the screen
# it exits otherwise
input()
