from locators.book_locator import BookLocator


class BookParser:

    def __init__(self, parent):
        self.parent = parent

    @property
    def title(self):
        locator = BookLocator.TITLE
        book_title = self.parent.select_one(locator).attrs["title"]
        # print(book_title)
        return book_title

    @property
    def link(self):
        locator = BookLocator.LINK
        book_link = self.parent.select_one(locator).attrs["href"]
        # print(book_link)
        return book_link

    @property
    def price(self):
        locator = BookLocator.PRICE
        return float(self.parent.select_one(locator).string[1:])

    @property
    def ratings(self):
        locator = BookLocator.RATING
        return self.parent.select_one(locator).attrs["class"][1]
