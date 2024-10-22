import random

word_list = ["Apple", "Chair", "Bread", "Flute", "Storm", "Green", "Light", "Clock", "Frame", "Dance", "Beach", "Blaze", "Crisp", "Quest", "Scale", "Spicy", "Toast", "Vivid", "Zebra", "Royal", "Earth", "Funky", "Grape", "Hasty", "Jolly", "Knead", "Lemon", "Mirth", "Night", "Quest"]

running = True

while running:
    picked_word = random.choice(word_list).lower()
    
    print("Welcome to Wordle!")

    dashes = []

    for i in range(len(picked_word)):
        dashes.append("_")

    print("".join(dashes))

    guesses = 0

    guessed = False

    while guessed == False and guesses < 6:
        pick = input("Enter your guess: ").lower()
        if len(pick) != 5:
            print("Invalid input. Please enter a 5 letter word.")
            continue

        guesses += 1   

        if pick == picked_word:
            print(f"You win! It took you {guesses} guesses.")
            guessed = True
            break

        for i in range(len(pick)):
            if pick[i] in picked_word:
                if pick[i] == picked_word[i]:
                        dashes[i] = pick[i].upper()
                else:
                    dashes[i] = pick[i]
                

                if "".join(dashes) == picked_word.upper():
                    print(f"You win! It took you {guesses} guesses.")
                    guessed = True
                    break

        print("".join(dashes))
    else:
        print(f"You lose! The word was {picked_word.upper()}")

    
    play_again = input("Would you like to play again? (yes or no) ").lower()

    if play_again == "no":
        running = False




