print("Welcome to the shopping cart program!")

cart = []
price = []

running = True

while running:

    print("Select one of the following options: \n 1. Add item \n 2. View cart \n 3. Remove Item \n 4. Compute Total \n 5. Quit \n (Be sure to enter the number of the option you would like to select.)")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item you would like to add: ")
        cart.append(item)

        item_price = float(input("Enter the price of the item: "))
        price.append(item_price)

        print(f"{item} has been added to the cart.")

    elif choice == "2":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart: ")
            for i in range(len(cart)):
                print(f"{cart[i]:<15} ${price[i]:.2f}")
            print("\n")

    elif choice == "3":
        item = input("Enter the item you would like to remove: ")
        if item in cart:
            price.remove(price[cart.index(item)])
            cart.remove(item)

            print(f"{item} has been removed from the cart.")
        else:
            print(f"{item} is not in the cart.")
        print("\n")

    elif choice == "4":
        total = 0
        for item in price:
            total += item
        print(f"Total: ${total:.2f} \n")

    elif choice == "5":
        running = False
        print("Thank you for shopping with us! \n")

    else:
        print("Invalid choice. Please enter a number between 1 and 5. \n")


    
