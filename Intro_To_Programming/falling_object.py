#Calculate the speed of a falling object 

import math

print("Please enter the following values to calculate the speed of a falling object: ")

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
a = float(input("Cross-sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for a sphere, 1.1 for a cylinder): "))

c = (1/2) * p * a * C

print(f"The inner value of c is {c:.3f}")

v = math.sqrt((m * g) / c) * (1 - math.exp((-math.sqrt(m * g * c) / m)* t)) 

print(f"The speed of the falling object is {v:.3f} m/s.")

v_terminal = math.sqrt(m * g / c)

print(f"The terminal velocity is {v_terminal:.3f} m/s.")