def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(
                f"Tittle: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}\n")
    else:
        print("No Book found in the System")