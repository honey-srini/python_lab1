# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input("Enter the decimal number :"))
print("The binary value of " ,dec, " is :" )
convertToBinary(dec)




    
