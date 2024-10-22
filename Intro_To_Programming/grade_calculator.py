# Grade Calculator

grade = float(input("Enter your grade percent: "))

letter = ""
plus_minus = ""

if grade >= 90:
    letter = "A"
    if grade <= 93:
        plus_minus = "-"
elif grade >= 80:
    letter = "B"
    if grade >= 87:
        plus_minus = "+"
    elif grade <= 83:
        plus_minus = "-"
elif grade >= 70:
    letter = "C"
    if grade >= 77:
        plus_minus = "+"
    elif grade <= 73:
        plus_minus = "-"
elif grade >= 60:
    letter = "D"
    if grade >= 67:
        plus_minus = "+"
    elif grade <= 63:
        plus_minus = "-"
else:
    letter = "F"

print(f"Your grade is: {letter}{plus_minus}")

if grade >= 70:
    print("You passed!")
else:
    print("You failed!")