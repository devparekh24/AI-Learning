from locators.book_locator import BookLocator


class BookParser:

    RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Book: {self.title}, its price is £{self.price} and rating is {self.ratings} star>"

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
        rating_string = self.parent.select_one(locator).attrs["class"][1]
        rating_number = BookParser.RATINGS[rating_string]
        return rating_number
