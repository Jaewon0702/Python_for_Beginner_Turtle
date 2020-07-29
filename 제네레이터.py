def getfunc(num):
    for i in range(0,num) :
        yield i
        print('제네레이터 진행 중')

for data in getfunc(5) :
    print(data)
