date=int(input("ENTER THE DATE : "))
month=int(input("ENTER THE MONTH : "))
year=int(input("ENTER THE YEAR : "))
if(date>0 and date<32)& (month<=12):
    print("THE DATE IS VALID")
else:
    print("THE DATE IS INVALID")
