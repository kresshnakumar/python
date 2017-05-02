def fibo(n):
    if n == 0:
        print '0'
    elif n == 1:
        print '0\n1'
    elif n > 1:
        firstNum = 0;
        secondNum = 1;
        print '0\n1'
        i = 2
        while i < n:
            thirdNum = firstNum + secondNum
            print thirdNum
            firstNum = secondNum
            secondNum = thirdNum
            i = i+1
fibo(10)
