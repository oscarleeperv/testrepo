from random import randint

def dice_roll():
	"""Choose a random number from 1 to 6 and print it."""
	number = randint(1, 6)
	print(number)
playing = True

while playing == True:
	roll_action = input("Press E to roll the dice and W to quit! ")
	if roll_action.lower() == 'e':
		dice_roll()
	elif roll_action.lower() == 'w':
		print("Goodbye!")
		playing = False