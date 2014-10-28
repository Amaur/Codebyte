def fibo(n):
    suma =0
    current_fib, next_fib = 1,1
    #l=[]
    i=0
    while i<n:
        #suma +=next_fib
        #l.append(next_fib)
        current_fib , next_fib = next_fib, current_fib + next_fib
        i+=1
        if(next_fib>4000000):
            break
        else:
            if(next_fib%2==0):
                suma +=next_fib


    return (suma)


print(fibo(150))
#4613732