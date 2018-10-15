# This is a guess the number game.

import random

def guessTheNumber():
	wrong_guesses = 0
	random_number = random.randint(0, 20)
	print (random_number)

	print ("I am think of a number between 1 and 20.")

	while True:
		try:

			userInput = int(input("Take a guess: "))
			
			if userInput < random_number:

				wrong_guesses +=1
				print ("Your guess is too low.")

			elif userInput > random_number:
				wrong_guesses +=1
				print ("Your guess is too high.")

			elif userInput == random_number:
				wrong_guesses +=1
				return "Good job! You guessed my number in " +str(wrong_guesses)+ " guesses!"
			
		except ValueError:
			wrong_guesses +=1
			print("Error: Invalid input")


print (guessTheNumber())

