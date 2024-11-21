from SimpleLibraryManagementSystem.add_book import add_book
from SimpleLibraryManagementSystem.view_all_books import view_all_books
from SimpleLibraryManagementSystem.update_book import update_book
from SimpleLibraryManagementSystem.remove_book import remove_book
from SimpleLibraryManagementSystem.load_books import load_books
from SimpleLibraryManagementSystem.save_all_books import save_all_books

all_books = load_books()

while True:
    print("\n***Welcome to Library Management System***")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove Book")

    menu = input("Input your Choice: ")

    if menu == "0":
        save_all_books(all_books)
        print("***Thanks for using Library Management System***")
        break
    elif menu == "1":
        all_books = add_book(all_books)
    elif menu == "2":
        view_all_books(all_books)
    elif menu == "3":
        all_books = update_book(all_books)
    elif menu == "4":
        all_books = remove_book(all_books)
    else:
        print("Choose a valid option!")
