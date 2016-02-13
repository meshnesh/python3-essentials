import time

choice = 0


print('Pending class assignments')
print(' ')
print('1, Websites')
print('2, User Experience')
print('3, Toy Problems')
print('4, Python')
print('5, None of them')

while True:
	try:
		while (choice < 1) or (choice > 5):
			choice = int(input("Which assignments have you not completed?"))
			break
	except ValueError:
		print("please type in a number!")


if choice == 1:
	print("Frank is gonna get you")

elif choice == 2:
	print("Sam is will fry you")

elif choice == 3:
	print("Ian and Nelson are gonna be mad")

elif choice == 4:
	print("Chencha is gonna burry you")

elif choice == 5:
	print("R.I.P my friend")


time.sleep(3)

print("Thank for your response")

time.sleep(2)