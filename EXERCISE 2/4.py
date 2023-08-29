num = int(input("ENTER THE NUMBER : "))
if(num<0):
    print("ENTER THE POSITIVE NUMBER ")
else:
    sum=0
    while(num > 0):
        sum += num
        num -= 1
print("THE SUM IS : ",sum)
