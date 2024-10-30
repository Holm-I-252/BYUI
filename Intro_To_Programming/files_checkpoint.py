book_list = open("Intro_To_Programming/book_list.txt", "r")
books = book_list.readlines()

for book in books:
    print(book)