people = int(input("enter the number of people"))
cats = int(input("enter the number of cats"))
dogs = int(input("enter the number of dogs"))
if people<cats:
	print("Too many cats! The world is doomed")
elif people>cats:
	print("Not many cats! The world is saved")
elif people>dogs:
	print("The world is Dry")
elif people<dogs:
	print("The world is drooled on!")
dogs +=5
if people>=dogs:
	print("People are greater than or equal to dogs")
elif people<=dogs:
	print("People are less than or equal to dogs")
elif people==dogs:
	print("People are dogs")
else:
	print("The world is full of aliens")
