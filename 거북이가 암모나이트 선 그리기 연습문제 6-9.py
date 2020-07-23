import turtle
import random

swidth,sheight,psize,dist=500,500,3,5
r,g,b,angle=[0]*4

turtle.title('거북이가 소라 모양 선 그리기')
turtle.shape('turtle')
turtle.pensize(psize)
turtle.setup(width=swidth+30,height=sheight+30)
turtle.screensize(swidth,sheight)

for _ in range(80) :
    r=random.random()
    g=random.random()
    b=random.random()
    turtle.pencolor((r,g,b))
    turtle.speed(0)
    turtle.forward(dist)
    turtle.left(angle)
    dist+=1
    angle=30



turtle.done()
