most_chapters = 0
most_chapters_book = ""

scripture = input("Enter the Standard work you would like to learn about: ")
print(f"\nYou entered: {scripture}\n")
with open("Intro_To_Programming/books_and_chapters.txt", "r") as file:
    for line in file:
        new_line = line.split(":")
        new_line[2] = new_line[2].replace("\n", "")
        print(new_line)
        if new_line[2] == f"{scripture}":
            print("check")
            print(f"Scripture: {new_line[2]} Book: {new_line[0]} Chapters: {new_line[1]}")

            if int(new_line[1]) > most_chapters:
                most_chapters = int(new_line[1])
                most_chapters_book = new_line[0]
            
print(f"\nThe book with the most chapters is {most_chapters_book} with {most_chapters} chapters.")
        