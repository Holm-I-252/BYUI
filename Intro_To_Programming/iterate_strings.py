word = "commitment"

fav_letter = input("Enter your favorite letter: ").lower()

for i in word:
    if i == fav_letter:
        print("_", end="")
    else:
        print(i, end="")

running = True

while running:
    quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

    num = int(input("\nEnter a number: "))

    for i, letter in enumerate(quote):
        if i % num == 0 and i != 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
        
    keep_going = input("\nWould you like to continue? (yes or no) ").lower()
    if keep_going == "no":
        running = False