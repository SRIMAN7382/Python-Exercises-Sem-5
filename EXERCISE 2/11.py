num = 356
temp=num
sum=0
while temp!=0:
    n=temp%10
    sum+= n*n*n
    temp=temp//10
if sum==num:
    print("GIVEN IS AMSTRONG NUMBER")
else:
    print(False)
