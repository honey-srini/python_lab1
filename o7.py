start=int(input("Enter the starting value :"))
end=int(input("Enter the ending value :"))
for n in range(start,end+1):
      if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)
    
