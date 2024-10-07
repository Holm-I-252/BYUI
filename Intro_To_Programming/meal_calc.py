child_meal_price = float(input("How much does a child's meal cost? "))
adult_meal_price = float(input("How much does an adult's meal cost? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))
print()

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

print(f"Subtotal: ${subtotal:.2f}")

total_tax = subtotal * (tax / 100)

print(f"Sales Tax: ${total_tax:.2f}")

total_price = subtotal + total_tax

print(f"Total: ${total_price:.2f}")
print()

tip = 0

add_tip = input("Would you like to leave a tip? (yes/no) ")

if add_tip == "yes":
    percent = input("How much would you like to leave? 15%, 20%, or 25%? ")
    if percent == "15":
        tip = total_price * 0.15
    elif percent == "20":
        tip = total_price * 0.20
    else:
        tip = total_price * 0.25

    print(f"Tip: ${tip:.2f}")
    print(f"Total with tip: ${total_price + tip:.2f}")
    print()
    

ammount_paid = round(float(input("How much did you pay? ")), 2)

change = ammount_paid - total_price - tip

print(f"Change: ${change:.2f}")