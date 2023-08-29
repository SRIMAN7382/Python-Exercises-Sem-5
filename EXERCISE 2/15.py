def prime(x):
    for i in range(2,x//2):
        if x%i==0:
            return False
    return True
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(2, x + 1):
       if x % i == 0 and prime(x):
           print(i)

num =10 
print_factors(num)
