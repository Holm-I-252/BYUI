shopping_list = []

running = True

while running:
    item = input("Enter an item to add to the list: (Enter 'stop' to end) ")
    
    if item == "stop":
        running = False
        break

    shopping_list.append(item)


for item in shopping_list:
    print(item)

for i in range(len(shopping_list)):
    print(f"{i}: {shopping_list[i]}")

change_index = int(input("Enter the index of the item you would like to change: "))
new_item = input("Enter the new item: ")

shopping_list[change_index] = new_item

for item in shopping_list:
    print(item)