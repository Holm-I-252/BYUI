running = True

names = []

while running:
    name = input("Enter a name: ")
    if name == "end":
        running = False
        break
    names.append(name)
    
print("Your friends are: ")
for name in names:
    print(name)