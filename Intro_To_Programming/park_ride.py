can_ride = False

p1_age = int(input("Enter the age of person 1: "))
p1_height = int(input("Enter the height of person 1 in inches: "))

p1_ticket = input("Does person 1 have a golden ticket? (yes or no) ").lower()

if p1_ticket == "yes":
    p1_age = 18

is_p2 = input("Is there a second person? (yes or no) ").lower()

if is_p2 == "yes":
    p2_age = int(input("Enter the age of person 2: "))
    p2_height = int(input("Enter the height of person 2 in inches: "))

    p2_ticket = input("Does person 2 have a golden ticket? (yes or no) ").lower()

    if p2_ticket == "yes":
        p2_age = 18

    if p1_height >= 36 and p2_height >= 36:
        if p1_age >= 18 or p2_age >= 18:
            can_ride = True
        elif p1_age >= 12 and p2_age >= 12 and p1_height >= 52 and p2_height >= 52:
            can_ride = True
        elif p1_age + p2_age >= 30:
            can_ride = True

else:
    if p1_height >= 62 and p1_age >= 18:
        can_ride = True

if can_ride:
    print("\nEnjoy the ride!\n")
else:
    print("\nSorry, you cannot ride.\n")