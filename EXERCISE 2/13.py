num=input("ENTER NUMBER TO CHECK : ")
revnum=0
for i in range(len(num)//2):
    if num[i]==num[len(num)-i-1]:
        revnum+=1
if revnum==len(num)//2:
    print(True)
        
