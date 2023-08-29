def parti(lst):
    even=[]
    odd=[]
    for i in lst:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    print("EVEN LIST : ",even)
    print("ODD LIST : ",odd)

lst=[4,1,6,7,5,9,8,10]
parti(lst)
