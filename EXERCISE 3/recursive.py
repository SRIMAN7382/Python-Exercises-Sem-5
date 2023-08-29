def rgcd(a,b):
    if a==b:
        return a
    elif a < b:
        return rgcd(b,a)
    else:
        return rgcd(b,a-b)
def rfib(n):
    if n==1:
        return 1
    else:
        return rfib(n-1)*n
def rrev(n,r):
    if n==0:
        return r
    else:
        return rrev(n//10,r*10+n%10)
    n=3567
    return rrev
    
