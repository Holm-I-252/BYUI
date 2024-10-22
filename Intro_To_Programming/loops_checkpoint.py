running = True

while running:
    num = int(input("Enter a positive number: "))
    if num < 0:
        print("Invalid input. Please try again.")
    else: 
        running = False
        print("Thank you for entering a positive number.")


candy_running = True

while candy_running:
    yes_or_no = input("Can I have a piece of candy? ").lower()
    if yes_or_no == "yes":
        print("Thank you!")
        candy_running = False