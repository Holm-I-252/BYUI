num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 < num_2:
    print(f"{num_1} is less than {num_2}")
else:
    print(f"{num_1} is equal to {num_2}")

favorite_animal = input("What is your favorite animal? ").lower()

if favorite_animal == "dog":
    print("That's my favorite animal too!")
else:
    print("That one's not my favorite.")