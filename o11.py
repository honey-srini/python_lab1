n=int(input("Enter the n no of number :"))
sum=0
for i in range(1,n+1):
    sum=sum+(i**3)
print("The sum of cube of first " , n , " natural number is ",sum)
