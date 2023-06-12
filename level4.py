game_type = input("Guess(type guess) a number or pick(type pick) a number? ")

print("Number guessing game:")

import random

correct = False
guesses = 3
computer_guesses = 1
user_number = int(input("Enter a number between 1 and 10: "))
random_number = random.randint(1,10)
print(user_number)

while not correct and guesses > 0 and game_type == "guess":
    # print("Player is guessing")
    print()
    print("Number of guesses remaining: " + str(guesses))
    user_number = int(input("Enter a number between 1 and 10: "))
    if  user_number == random_number:
        correct = True
        print("Congrats! You guessed the number!")
    elif user_number < random_number:
        guesses = guesses- 1
        print("Too low")
    elif user_number > random_number:
        guesses = guesses - 1
        print("Too high")

while not correct and game_type == "pick":
    # print("Computer is guessing")
    print(random_number)
    if  random_number == user_number:
        correct = True
        print("The computer guessed your number in " + str(computer_guesses) + " attempts!")
    elif random_number < user_number:
        random_number = random.randint(random_number,10)
        computer_guesses = computer_guesses + 1
    elif random_number > user_number:
        random_number = random.randint(1,random_number)
        computer_guesses = computer_guesses + 1