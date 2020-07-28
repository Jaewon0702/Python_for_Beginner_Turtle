import turtle
from tkinter.simpledialog import *
import math
import random

instr=''
swidth,sheight=500,500
tx,ty,angle=[0]*3

turtle.title('원을 그리면서 글자를 쓰는 거북이')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()

instr=askstring('문자열 입력','거북이 쓸 문자열 입력')
for ch in instr :
    angle+=360/len(instr)
    tx=200*math.cos(math.radians(angle))
    ty=200*math.sin(math.radians(angle))
    r=random.random(); g=random.random(); b=random.random();

    txtsize=20 
    turtle.goto(tx,ty)
    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은 고딕',txtsize,'bold'))

turtle.done()
