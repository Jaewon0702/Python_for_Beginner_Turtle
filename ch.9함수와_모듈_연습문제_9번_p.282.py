def myrange(start,end,hop=1) :
    retval=start
    while retval<=end :
        yield retval
        retval+=hop

hap=0
for i in myrange(1,5,2):
    hap+=i
a=int(input('예상 값을 입력하시요.'))
print(a==hap)
