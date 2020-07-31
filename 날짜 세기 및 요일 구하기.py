from time import *
from datetime import *

def countdays(date1,date2) :
    retdays=0
    year,month,day=date1.split('/')
    sday=date(int(year),int(month),int(day))
    year,month,day=date2.split('/')
    eday=date(int(year),int(month),int(day))
    diffdays=eday-sday
    retdays=diffdays.days
    return retdays

def getday(t) :
    weeks=['월','화','수','목','금','토','일']
    return weeks[t.tm_wday]

startdate,curdate,tm='','',None

startdate=input('시작 날짜(연/월/일)-->')
tm=localtime()
curdate=str(tm.tm_year)+'/'+str(tm.tm_mon)+'/'+str(tm.tm_mday)
print("%s부터 오늘 (%s)까지는 %s일이 지났습니다."%(startdate,curdate,countdays(startdate,curdate)))
print("그리고 오늘은 %s요일 입니다."%(getday(tm)))
