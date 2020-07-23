import turtle
i,k,tx,ty=[0]*4
swidth,sheight=800,450

turtle.title('거북이로 구구단 출력하기')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
tx,ty=-500,250
turtle.goto(tx,ty)

for i in range(1,10) :
    for k in range(2,10) :
        turtle.goto(tx+80*k,ty-40*i)
        gugu=str(k)+'x'+str(i)+'='+str(k*i)
        turtle.write(gugu,font=('Arial','12','bold'))

turtle.done()
