#loops back to start to play again
play_again = "y"
while play_again =="y":

#introduction and gives random number
    print("I'm thinking of a number between 1-100.")
    import random
    random_number = random.randint(1, 100)
    user_guess = int(input("Enter your guess: "))

 #make user enter valid number
    while user_guess < 1 or user_guess > 100:
        print("Invalid guess, please try again.")
        user_guess = int(input("Enter your guess: "))

#guide user whether guess is too high or too low
    number_guesses = 1
    while user_guess != random_number:
        number_guesses = number_guesses + 1
        if user_guess > random_number:
            user_guess = int(input("Guess lower: "))
        elif user_guess < random_number: 
            user_guess = int(input("Guess higher: "))
        elif user_guess == random_number: 
            print("Congratulations, you win!")

  #calculates number of guesses and gives feedback
    if number_guesses <= 3:
        print("You are amazing")
    elif number_guesses <= 5:
        print("Impressive")
    elif number_guesses <= 7:
        print("Good Job")
    elif number_guesses <= 9:
        print("Took a little longer, but you got it!")
    elif number_guesses >= 10:
        print("You need to lock in")

#gives option to play again
    play_again = input("To play again, press y: ")