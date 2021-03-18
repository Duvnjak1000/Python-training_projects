import random

secret = random.randint (1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " +str(secret))
        break
    elif guess > secret:
        print("Sorry, your guess is not correct...Try smaller value than specified ")
    elif guess < secret:
        print("Sorry, your guess is not correct...Try higher value than specified ")
