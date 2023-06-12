print("hello")

import random

correct = False
guesses = 3
random_number = random.randint(1,10)
print(random_number)

while not correct and guesses > 0:
    print(guesses)
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