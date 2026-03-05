import requests
from pages.books_page import BooksPage

PAGE_URL = "http://books.toscrape.com/"
page_content = requests.get(PAGE_URL).content
# print(page_content)
books_page = BooksPage(page_content)
books = books_page.books
# print(books_page)
# for book in books:
#     print(book)
#     print(book.title)
#     print(book.link)
#     print(book.price)
#     print(book.ratings)
#     print("-" * 100)
