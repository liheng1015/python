def mk_fib(n):
    fib = [0,1]
    #n = int(input('长度:'))
    for i in  range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib #print(fib)
a = mk_fib(6)
#alist = [i * 2 for i in a]
print(a)
