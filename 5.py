en=int(input("ENTER THE MARKS IN ENGLISH: "))
mat=int(input("ENTER THE MARKS IN MATHS :"))
sci=int(input("ENTER THE MARKS IN SCIENCE :"))
avg=(en+mat+sci)/3
print(avg)
if(en>89):
    print(en)
elif(mat>89):
    print(mat)
elif(sci>89):
    print(sci)
