num =154789
revnum=0
while num!=0:
    temp=num%10
    revnum=revnum*10+temp
    num//=10
print("REVERSED NUM IS : "+str(revnum))
