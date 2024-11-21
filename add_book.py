from SimpleLibraryManagementSystem.save_all_books import save_all_books


def add_book(all_books):
    title = input("Enter the books' title: ")
    author = input("Enter the authors name: ")
    isbn = int(input("Enter the ISBN: "))
    year = int(input("Enter the Publishing year: "))
    price = float(input("Enter the Book price: "))
    quantity = int(input("Enter the remaining quantity: "))

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" :price,
        "quantity": quantity
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Book added Successfully")

    return all_books


