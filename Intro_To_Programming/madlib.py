running = True

while running:

    print("Madlib! Please enter the following information:")

    choose_inputs = True

    while choose_inputs:
        adjective = input("An adjective: ")
        animal = input("An animal: ")
        verb = input("A verb: ")
        exclamation = input("An exclamation: ")
        verb_1 = input("A verb: ")
        verb_2 = input("Another verb: ")

        confirm = input("Are you happy with your choices? (yes/no) ")
        if confirm == "yes":
            choose_inputs = False

    print("Here is your madlib: ")

    print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. "{exclamation}!" I yelled. But all I could think to do was to {verb_1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_2} right in front of my family.')

    again = input("Would you like to play again? (yes/no) ")
    if again == "no":
        running = False
        print("Thanks for playing!")
