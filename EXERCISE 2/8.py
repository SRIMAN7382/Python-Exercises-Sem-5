ch=int(input("ENTER THE CHOICE : "))
 while ch==1:
    num1=int(input("ENTER THE NUMBER 1 : "))
    num2=int(input("ENTER THE NUMBER 2 : "))
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        break
    else:
        lcm=lcm+1
print("LCM IS :",lcm)
while ch==2:
    num1=int(input("ENTER THE NUMBER 1 : "))
    num2=int(input("ENTER THE NUMBER 2 : "))
   for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD of", num1, "and", num2, "is", gcd)
    
    
