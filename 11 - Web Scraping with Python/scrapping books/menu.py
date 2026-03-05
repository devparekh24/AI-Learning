from app import books


def best_book_by_rating():
    best_ten_books = sorted(books, key=lambda book: book.ratings * -1)[:10]
    for book in best_ten_books:
        print(book)


def cheapest_book_by_price():
    cheapest_ten_books = sorted(books, key=lambda book: book.price)[:10]
    for book in cheapest_ten_books:
        print(book)


print("-" * 25, "Best Books by Rating", "-" * 25)
best_book_by_rating()
print("-" * 25, "Cheapest Books by Price", "-" * 25)
cheapest_book_by_price()
