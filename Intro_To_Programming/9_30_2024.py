#Notes 9/30/24 - Intro to Programming - Variables and Expressions

#input 2 numbers and converts the input to an integer (whole number)

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

#output the sum of the 2 numbers

print(f"{num_1} + {num_2} = {num_1 + num_2}")

#You can also do other types of math operations

print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")
print(f"{num_1} / {num_2} = {num_1 / num_2}")

#You can also do the same thing with floats (numbers with decimals)

num_3 = float(input("Enter a number: "))
num_4 = float(input("Enter another number: "))

print(f"{num_3} + {num_4} = {num_3 + num_4}")

#You can do exponents as well

print(f"{num_3} ** {num_4} = {num_3 ** num_4}")

#You can also find the remainder of 2 numbers by using the modulus operator %. It's useful for doing things like finding even and odd numbers.

print(f"{num_1} % {num_2} = {num_1 % num_2}")

#You can also do floor division, which is division that rounds down to the nearest whole number.

print(f"{num_1} // {num_2} = {num_1 // num_2}")

