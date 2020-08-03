from tkinter import *
fnameList=["1582056968259-5.gif","1582344649136.gif","1582344926788.gif","1582420194152.gif",
        "1582432139652.gif","1582435544531-15.gif","1582829077978-2.gif","1582829098728.gif","1582958291517.gif","1583203510556.gif",
        "1583203522888.gif", "1583203539183.gif", "1583203557038.gif", "1583203563320.gif", "1583304553170.gif","1583304567281.gif","1583304736592.gif" ]
photoList=[None]*9
num=0

def clickNext() :
    global num
    num+=1
    if num>16 :
        num=0
    photo=PhotoImage(file="미국 서부 사진/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

def clickPrev() :
    global num
    num-=1
    if num<0 :
        num=16
    photo=PhotoImage(file="미국 서부 사진/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo

window=Tk()
window.geometry("750x960")
window.title("사진 앨범 보기")

btnPrev=Button(window,text="<<Prev",command=clickPrev)
btnNext=Button(window,text="Next>>",command=clickNext)

photo=PhotoImage(file="미국 서부 사진/"+fnameList[0])
pLabel=Label(window,image=photo)

btnPrev.place(x=250,y=10)
btnNext.place(x=400,y=10)
pLabel.place(x=15,y=40)

window.mainloop()


    
