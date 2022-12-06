
odd_count = 0
even_count = 0

while True:
    num = int(input("Input an integer (-1 terminates): "))
    if num == -1:
        break
    if num < 1:
        continue
    if num % 2 == 0:
        even_count += 1
        
    if num %2==1:
        odd_count += 1
        

print("Even count:", even_count)
print("Odd count:", odd_count)

