from turtle import *
pensize(50)
pencolor('blue')
forward(250)
pencolor(0,1.0,0)
forward(250)
pensize(10)
goto(-400,50)


for red in range(4):
    for green in range(4):
        for blue in range(4):
            pencolor(red/4.0,green/4.0,blue/4.0)
            forward(10)
            

