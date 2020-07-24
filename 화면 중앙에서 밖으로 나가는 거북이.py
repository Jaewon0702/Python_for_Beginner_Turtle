#거북이 정보 [[거북이1,X,Y,크기,R,G,B],[거북이2,X,Y,크기,,R,G,B...]]
import turtle
import random
myturtle,tx,ty,tcolor,tsize,tshape=[None]*6
shapelist=[]
playerturtles=[]
swidth,sheight=500,500

turtle.title('화면 중앙에서 밖으로 나가는 거북이')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)

shapelist=turtle.getshapes()
for i in range(0,100) :
    random.shuffle(shapelist) #myturtle=turtle.Turtle(random.choice(shapelist))
    myturtle=turtle.Turtle(shapelist[0])
    tx=random.randrange(-swidth/2,swidth/2)
    ty=random.randrange(-sheight,sheight)

    r=random.random();g=random.random();b=random.random()
    tsize=random.randrange(1,3)
    playerturtles.append([myturtle,tx,ty,tsize,r,g,b])

for tlist in playerturtles :
    myturtle=tlist[0]
    myturtle.color((tlist[4],tlist[5],tlist[6]))
    myturtle.pencolor((tlist[4],tlist[5],tlist[6]))
    myturtle.turtlesize(tlist[3])
    myturtle.goto(tlist[1],tlist[2])
    

turtle.done()

