num = int(input("ENTER THE NUMBER TO CHECK : "))
if num>1:
    for i in range(2,int(num/2)+1):
        if(num % i)==0:
            print(num,"IS NOT A PRIME NUMBER")
            break
    else:
        print(num,"IS NOT A PRIME NUMBER")
else:
    print(num,"is a prime number")
