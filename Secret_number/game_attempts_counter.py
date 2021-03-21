import random

secret = random.randint(1, 30)
attempts = 0


    #This will:
#open the score.txt file,
#read its contents,
#save it into the variable named best_score,
#and print it in the Terminal.

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1
                                                              #We can compare our best_score to the number of attempts and see which one is a lower number (remember: lower is better).
    if guess == secret:                                       #If attempts is lower than best_score, we write the attempts number into the file
            if attempts < best_score:
                with open("score.txt", "w") as score_file:
                    score_file.write(str(attempts))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
