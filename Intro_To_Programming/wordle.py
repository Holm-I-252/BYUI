import random

word_list = ["Apple", "Chair", "Bread", "Flute", "Storm", "Green", "Light", "Clock", "Frame", "Dance", "Beach", "Blaze", "Crisp", "Quest", "Scale", "Spicy", "Toast", "Vivid", "Zebra", "Royal", "Earth", "Funky", "Grape", "Hasty", "Jolly", "Knead", "Lemon", "Mirth", "Night", "Quest"]

running = True

while running:
    picked_word = random.choice(word_list).lower()
    print(picked_word)
    
    print("Welcome to Wordle!")

    dashes = []

    for i in range(len(picked_word)):
        dashes.append("_")

    print("".join(dashes))

    guesses = 6

    while guesses > 0:
        pick = input("Enter a letter: ").lower()

        if pick in picked_word:
            for i in range(len(picked_word)):
                if pick == picked_word[i]:
                    dashes[i] = pick
            print("".join(dashes))

            if "_" not in dashes:
                print("You win!")
                break

            guesses -= 1
        else:
            guesses -= 1
            print("".join(dashes))

    else:
        print(f"You lose! The word was {picked_word}")






    running = False