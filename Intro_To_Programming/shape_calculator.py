import math

#Ask the user for one measurement or multiple

running = True

while running:
    num_of_nums = input("Do you want one meausrement or multiple? ")

    if num_of_nums == "one":

        length = float(input("Enter the length: "))

        s_area = length ** 2

        print(f"The area of the square is {s_area}")

        c_area = math.pi * length ** 2

        print(f"The area of the circle is {c_area}")

        cube_volume = length ** 3

        print(f"The volume of the cube is {cube_volume}")

        sphere_volume = (4/3) * math.pi * length ** 3

        print(f"The volume of the sphere is {sphere_volume}")

    else:

        #Area for a square

        s_side = float(input("Enter the side length of the square in cm: "))

        s_area = s_side ** 2

        print(f"The area of the square in cm is {s_area}")
        print(f"The area of the square in m is {s_area / 10000}")

        #Area for a rectangle

        r_length = float(input("Enter the length of the rectangle in cm: "))
        r_width = float(input("Enter the width of the rectangle in cm: "))

        r_area = r_length * r_width

        print(f"The area of the rectangle in cm is {r_area}")
        print(f"The area of the rectangle in m is {r_area / 10000}")

        #Area for a circle

        c_radius = float(input("Enter the radius of the circle in cm: "))

        c_area = math.pi * c_radius ** 2

        print(f"The area of the circle in cm is {c_area}")
        print(f"The area of the circle in m is {c_area / 10000}")

    keep_going = input("Do you want to calculate another area? (yes/no) ")

    if keep_going == "no":
        running = False
        print("Stopping program...")
