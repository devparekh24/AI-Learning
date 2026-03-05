import requests
from pages.quotes_page import QuotesPage

PAGE_URL = "http://quotes.toscrape.com/"
page_content = requests.get(PAGE_URL).content
# print(page_content)
page = QuotesPage(page_content)
print(page)
print(type(page))

for p in page.quotes:
    print(p)
    print("-" * 100)
    print(p.content)
    print("-" * 100)
    print(p.author)
    print("-" * 100)
    print(p.tags)
    print("-" * 100)
