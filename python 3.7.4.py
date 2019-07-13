# setheading(heading)
# will change the current direction to the heading angle
from turtle import *
colors = ['blue','red','purple','orange','green','yellow']
for angle in range(0,360,15):
    pencolor(colors[angle%6])
    setheading(angle)
    forward(100)
    write(str(angle)+ 'o')
    backward(100)
    
