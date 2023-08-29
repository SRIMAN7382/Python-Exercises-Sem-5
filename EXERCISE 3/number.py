def sumofdigit(n):
    sum=0
    while(n != 0):
        sum= sum + (n % 10)
        n=n//10
    return sum
def revdigit(n):
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev
    
