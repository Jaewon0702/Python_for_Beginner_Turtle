def Fibonacci(n) :
    if n==0 :
        return 0
    elif n==1 :
        return 1
    elif n>=2 :
        return Fibonacci(n-1)+Fibonacci(n-2)
    else :
        return '잘못된 입력입니다.'

num=int(input("피보나치 수열 F(N)의 N값을 입력하세요.-->"))
print('F(%d)=%d'%(num,Fibonacci(num)))
    
        
