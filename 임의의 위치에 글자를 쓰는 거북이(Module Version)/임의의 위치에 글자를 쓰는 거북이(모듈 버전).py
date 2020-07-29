from myturtle import *
import turtle

instr=''
swidth,sheight=300,300
tx,ty,tangle,tsize=[0]*4

turtle.title('임의의 위치에 글자를 쓰는 거북이(모듈 버전')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

instr=getstring()

for ch in instr :
    tx,ty,tangle,txtsize=getxyas(swidth,sheight)
    r,g,b=getrgb()
    turtle.goto(tx,ty)
    turtle.left(tangle)

    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은 고딕',txtsize,'bold'))

turtle.done()
