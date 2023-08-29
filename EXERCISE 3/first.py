def Fibonacci(n):
    lst=[0,1]
    for x in range(n):
        print(lst[x])
        new=lst[x+1]+lst[x]
        lst.append(new)

