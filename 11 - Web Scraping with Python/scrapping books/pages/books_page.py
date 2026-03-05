from bs4 import BeautifulSoup
from locators.books_page_locator import BooksPageLocator
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def books(self):
        locator = BooksPageLocator.BOOK
        books_list = self.soup.select(locator)
        # print(books_list)
        return [BookParser(book) for book in books_list]
