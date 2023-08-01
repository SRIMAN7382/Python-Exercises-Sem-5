a=int(input("ENTER THE VALUE OF ANGLE A : "))
b=int(input("ENTER THE VALUE OF ANGLE B : "))
c=int(input("ENTER THE VALUE OF ANGLE C : "))
if(a<0,b<0,c<0):
    print("THE ANGLES DO NOT FORM TRIANGLE")

if(a+b+c==180):
    print("THE ANGLES FORM TRIANGLE")
else:
    print("THE ANGLES DO NOT FORM TRIANGLE")
