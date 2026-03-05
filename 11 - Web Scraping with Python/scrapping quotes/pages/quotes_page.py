from bs4 import BeautifulSoup
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quotes_lists = self.soup.select(locator)
        return [QuoteParser(ql) for ql in quotes_lists]
