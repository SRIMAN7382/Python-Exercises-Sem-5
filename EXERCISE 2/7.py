low= int(input ("Please, Enter the Low Value: "))  
hig = int(input ("Please, Enter the High Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (low, hig + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
