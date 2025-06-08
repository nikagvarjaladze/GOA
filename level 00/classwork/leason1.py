from turtle import *

speed(5)
width(4)
color("skyblue")

for i in range(4):
    forward(200)    #square
    left(90)



forward(70)
color("lightgreen")
left(90)
forward(100)
right(90)       #door
forward(60)
right(90)
forward(100)


penup()
goto(200,200)    #roof cordinates
pendown()


color("orange")
right(150)
forward(200)    #the roof itself
left(120)
forward(200)


penup()
goto(146,186)
pendown()

for i in range(4):
    forward(50)
    left(90)


penup()
goto(46,186)
pendown()


for i in range(4):
    forward(50)
    left(90)