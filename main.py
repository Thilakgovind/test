print("Hello, Welcome to the game!")
print("Welcome to the secret version!")

import random

def random_number():
    return random.randint(1, 100)

def main():
    while True:
        g = int(input("Guess a number between 1 and 100 (or 0 to exit): "))
        random_num = random_number()
        if g == 0:
            print("Exiting the game.")
            break
        elif g < 1 or g > 100:
            print("Please enter a valid number between 1 and 100.")
        elif g == random_num:
            print("Congratulations! You guessed the right number:", random_num)
            random_num = random_number()
        else:
            print("Wrong guess. The number was:", random_num)

main()
    
