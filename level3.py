print("hello")

import random

correct = False

user_number = int(input("Enter a number between 1 and 10: "))
random_number = random.randint(1,10)
print(user_number)

while not correct:
    
    print(random_number)
    if  random_number == user_number:
        correct = True
        print("The computer guessed your number!")
    elif random_number < user_number:
        random_number = random.randint(random_number,10)
    elif random_number > user_number:
        random_number = random.randint(1,random_number)