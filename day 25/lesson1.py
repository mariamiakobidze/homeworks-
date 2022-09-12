def first_non_consecutive(arr):
   i = 0
   while i < len(arr)-1:
       if arr[i+1] - arr[1] != 1:
           return arr[i+1]
        
        
from turtle import *

speed(0)


def draw_square():
    begin_fill()
    for i in range(4):
        color("green")
        width(3)

        forward(250)
        left(90)
    end_fill()


penup()
goto(-150, -150)
pendown()

draw_square()


def draw_triangle():
    begin_fill()
    for i in range(3):
        width(3)
        color("yellow")
        forward(250)
        left(120)

    end_fill()


penup()
goto(-150, 100)
pendown()


draw_triangle()


def draw_door():
    begin_fill()
    for i in range(4):
        width(2)
        color("blue")
        forward(120)
        left(90)
    end_fill()


penup()
goto(-80, -150)
width()
pendown()

draw_door()


def draw_window():
    begin_fill()
    for i in range(4):
        width(1)
        color("green")
        forward(60)
        left(90)
    end_fill()


penup()
goto(30, -10)
pendown()

draw_window()


def draw_window1():
    begin_fill()
    for i in range(4):
        color("orange")
        forward(60)
        left(90)
    end_fill()

penup()
goto(-140, -10)
pendown()

draw_window1()


def draw_chimeny():
    begin_fill()
    for i in range(1):

        color("brown")

        left(90)
        forward(45)
        right(90)
        forward(42)
        right(90)
        forward(126)
    end_fill()


penup()
goto(60, 170)
pendown()

draw_chimeny()


exitonclick()