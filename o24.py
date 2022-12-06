
# input the maximum number to
# which you want to send

print("Numbers not divisible by 2 and 4 from 1 to 100: ")

for i in range(1, 100, 2):
	
	# check if number is not divisible by 2 and 4
	if (i % 2 != 0) &(i %4 !=0):
		print(i)
