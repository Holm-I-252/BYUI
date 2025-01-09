def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return 3.14 * radius * radius

def compute_area(shape, side_1, side_2):
    if shape == "rectangle":
        return compute_area_rectangle(side_1, side_2)
    elif shape == "circle":
        return compute_area_circle(side_1)
    elif shape == "square":
        return compute_area_rectangle(side_1, side_1)
    else:
        return "Invalid shape"

running = True

while running:
    print("Choose a shape to calculate the area (Square, Rectangle, or circle) and the sides/radius:")
    choice = input("Enter your shape: ").lower()
    if choice == "exit":
        running = False
        break
    side_one = int(input("Enter the first side/radius: "))
    side_two = 0
    if choice == "rectangle":
        side_two = int(input("Enter the second side: "))
    print(compute_area(choice, side_one, side_two))
