import  random
"""This will allow us to pause the program at given times"""
import time
"""This is a boolean var"""
roll_again = "yes"

while roll_again == "yes" or roll_again == "Y":
	print("\nRolling the dice...")
	"""slept for one second"""
	time.sleep(1)

	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)

	print("The values are:")
	""" =" allows dice 1 & 2 value to be shown to screen"""
	print("Dice 1 =",dice1, "\nDice 2 =", dice2)

	if dice1 == dice2:
		print("You rolled a double!")
	else:
		print("Keep trying!")
	roll_again = input ("\nRoll the dice again (Y/N) ")

