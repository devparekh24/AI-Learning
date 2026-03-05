import requests
from pages.books_page import BooksPage

PAGE_URL = "http://books.toscrape.com/"
page_content = requests.get(PAGE_URL).content
# print(page_content)
books_page = BooksPage(page_content)
# print(books_page)
for book in books_page.books:
    # print(book)
    print("-" * 100)
    print(book.title)
    print("-" * 100)
    print(book.link)
    print("-" * 100)
    print(book.price)
    print("-" * 100)
    print(book.ratings)
    print("-" * 100)
