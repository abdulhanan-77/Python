import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than zero.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the random number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("Please type a number.")
        continue

    if user_guess == random_number:
        print("You got it.")
        break
    elif user_guess > random_number:
        print("Your guess is above the randomly generated number.")
    else:
        print("Your guess is below the randomly generated number.")

print("You got it right in", guesses, "guesses.")