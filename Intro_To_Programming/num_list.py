running = True

num_list = []

while running:
    num = int(input("Enter a number (Enter 0 to stop): "))
    if num == 0:
        running = False
    else:
        num_list.append(num)


print(f"The sum of the numbers is {sum(num_list)}")
print(f"The average of the numbers is {sum(num_list) / len(num_list)}")
print(f"The highest number is {max(num_list)}")

positive_list = []  

for i in num_list:
    if i > 0:
        positive_list.append(i)
        
print(f"The lowest positive number is {min(positive_list)}")
print(f"The sorted list of numbers is ")
sorted = sorted(num_list)

for i in sorted:
    print(i)