p=int(input("Enter the principal amount :"))
t=int(input("Enter the timespan (years) :"))
r=float(input("Enter the rate of intrest :")) 
a=p*(1+(r/100))**t 
ci=a-p 
print("The Compoun Intrest is : ",int(ci))
