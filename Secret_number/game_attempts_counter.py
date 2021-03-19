import random

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score: " + str(best_score))

    #This will:
#open the score.txt file,
#read its contents,
#save it into the variable named best_score,
#and print it in the Terminal.

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
