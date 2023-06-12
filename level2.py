print("hello")

import random

correct = False
guesses = 3

user_number = int(input("Enter a number between 1 and 10: "))
print(user_number)

while not correct and guesses > 0:
    random_number = random.randint(1,10)
    print(random_number)
    if  random_number == user_number:
        correct = True
        print("The computer guessed your number!")
    elif random_number < user_number:
        guesses = guesses- 1
    elif random_number > user_number:
        guesses = guesses - 1