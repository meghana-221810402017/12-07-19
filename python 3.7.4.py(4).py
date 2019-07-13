# hexagon with multi color
from turtle import *
colors = ['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100 + 1)
    forward(x)
    left(59)
