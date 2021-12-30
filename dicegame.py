import random

numbers = [1, 2, 3, 4, 5, 6]
random_number = random.choice(numbers)


while True:
    guess = int(input("Enter your guess [1-6]: "))
    if guess == random_number:
        print("Correct answer!")
        break
    else:
        print("Sorry, try again.")
        continue