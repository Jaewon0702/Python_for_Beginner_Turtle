import turtle
import math
import random
t1,t2,t3=[None]*3
t1X,t1Y,t2X,t2Y,t3X,t3Y=[0]*6
swidth,sheight=300,300
turtle.title('거북이가 서로 만나면 커지기')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)

t1=turtle.Turtle('turtle'); t1.color('red'); t1.penup()
t2=turtle.Turtle('turtle'); t2.color('green'); t2.penup()
t3=turtle.Turtle('turtle'); t3.color('blue'); t3.penup()

t1.goto(-100,-100);t2.goto(0,0);t3.goto(100,100)

while True :
    angle1=random.randrange(0,360);angle2=random.randrange(0,360);angle3=random.randrange(0,360)
    dist1=random.randrange(0,50);dist2=random.randrange(0,50);dist3=random.randrange(0,50)
    t1.left(angle1);t1.forward(dist1)
    t2.left(angle2);t2.forward(dist2)
    t3.left(angle3);t3.forward(dist3)
    t1.speed(0);t2.speed(0);t3.speed(0)

    t1X=t1.xcor();t1Y=t1.ycor()
    t2X=t2.xcor();t2Y=t2.ycor()
    t3X=t3.xcor();t3Y=t3.ycor()

    if math.sqrt(((t1X-t2X)*(t1X-t2X)+(t1Y-t2Y)*(t1Y-t2Y)))<=20 or\
       math.sqrt(((t1X-t3X)*(t1X-t3X)+(t1Y-t3Y)*(t1Y-t3Y)))<=20 or\
       math.sqrt(((t3X-t2X)*(t3X-t2X)+(t3Y-t2Y)*(t3Y-t2Y)))<=20 :
        t1.turtlesize(3); t2.turtlesize(3);t3.turtlesize(3)
        break
turtle.done()
       
                                        
                                        


