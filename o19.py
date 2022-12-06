new_videos = int(input("Enter the number of new videos: "))
old_videos = int(input("Enter the number of old videos: "))

days = int(input("Enter the number of days rented: "))
sum = (new_videos*75) + (old_videos*50)
total_cost = (sum*days)
print("The total cost  is","INR",total_cost)
