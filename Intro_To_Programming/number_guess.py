import random 

guesses = 0
guess = ""

running = True

while running:
    num = random.randint(1, 10)

    while guess != num:
        guess = int(input(f"Enter a number between 1 and 10. You have made {guesses} attempts."))
        
        if guess == num:
            print("You win!")
            break
        elif guess > num:
            print("Too high.")
            guesses += 1
        else:
            print("Too low.")
            guesses += 1
        
    play_again = input("Would you like to play again? (yes or no) ").lower()
    if play_again == "no":
        running = False
        break
    


    