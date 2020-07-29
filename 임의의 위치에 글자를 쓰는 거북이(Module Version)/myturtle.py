import random
from tkinter.simpledialog import *

def getstring() :
    retstr=''
    retstr=askstring('문자열 입력','거북이가 쓸 문자열 입력')
    return retstr

def getrgb() :
    r,g,b=0,0,0
    r=random.random()
    g=random.random()
    b=random.random()
    return (r,g,b)

def getxyas(sw,sh) :
    x,y,angle,size=[0]*4
    x=random.randrange(-sw/2,sw/2)
    y=random.randrange(-sh/2,sh/2)
    angle=random.randrange(0,360)
    size=random.randrange(10,50)
    return [x,y,angle,size]
