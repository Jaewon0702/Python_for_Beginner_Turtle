import turtle
import math
import random
t1,t2,t3,t4=[None]*4
t1X,t1Y,t2X,t2Y,t3X,t3Y,t4X,t4Y=[0]*8
swidth,sheight=300,300
turtle.title('거북이가 서로 만나면 커지기')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)

t1=turtle.Turtle('turtle'); t1.color('red'); t1.penup()
t2=turtle.Turtle('turtle'); t2.color('green'); t2.penup()
t3=turtle.Turtle('turtle'); t3.color('blue'); t3.penup()
t4=turtle.Turtle('turtle'); t4.color('purple'); t4.penup()

t1.goto(-100,-100);t2.goto(-100,100);t3.goto(100,100);t4.goto(100,-100)

while True :
    angle1=random.randrange(0,360);angle2=random.randrange(0,360);angle3=random.randrange(0,360)
    angle4=random.randrange(0,360)
    dist1=random.randrange(0,70);dist2=random.randrange(0,70);dist3=random.randrange(0,70)
    dist4=random.randrange(0,70)
    t1.left(angle1);t1.forward(dist1)
    t2.left(angle2);t2.forward(dist2)
    t3.left(angle3);t3.forward(dist3)
    t4.left(angle4);t4.forward(dist4)
    
    t1.speed(10);t2.speed(10);t3.speed(10);t4.speed(10)

    t1X=t1.xcor();t1Y=t1.ycor()
    t2X=t2.xcor();t2Y=t2.ycor()
    t3X=t3.xcor();t3Y=t3.ycor()
    t4X=t4.xcor();t4Y=t4.ycor()
    

    if math.sqrt(((t1X-t2X)*(t1X-t2X)+(t1Y-t2Y)*(t1Y-t2Y)))<=20 :
        t1.stamp(); t2.stamp()
        
    if math.sqrt(((t1X-t3X)*(t1X-t3X)+(t1Y-t3Y)*(t1Y-t3Y)))<=20 :
        t1.stamp();t3.stamp();
        
    if math.sqrt(((t1X-t4X)*(t1X-t4X)+(t1Y-t4Y)*(t1Y-t4Y)))<=20 :
        t1.stamp(); t4.stamp()
        
    if math.sqrt(((t3X-t2X)*(t3X-t2X)+(t3Y-t2Y)*(t3Y-t2Y)))<=20 :
        t2.stamp(); t3.stamp()
        
    if math.sqrt(((t2X-t4X)*(t2X-t4X)+(t2Y-t4Y)*(t2Y-t4Y)))<=20 :
        t2.stamp();t4.stamp()
        
    if math.sqrt(((t3X-t4X)*(t3X-t4X)+(t3Y-t4Y)*(t3Y-t4Y)))<=20 :
        t3.stamp(); t4.stamp()
        
turtle.done()
