import re
from bs4 import BeautifulSoup

ITEMLIST_HTML = """
<html>
<head></head>
<body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
  <article class="product_pod">
    <div class="image_container">
      <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
    </div>
    <p class="star-rating Three">
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
    </p>
    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
    <div class="product_price">
      <p class="price_color">£51.77</p>
      <p class="instock availability"><i class="icon-ok"></i>
        In stock
      </p>
      <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
      </form>
    </div>
  </article>
</li>
"""


class ParsedItemLocator:
    NAME_LOCATOR = "article.product_pod h3 a"
    LINK_LOCATOR = "article.product_pod h3 a"
    PRICE_LOCATOR = "article.product_pod p.price_color"
    RATINGS_LOCATOR = "article.product_pod p.star-rating"


class PasedItem:
    """
    A class to represent a parsed item. which take in HTML page (or part of it), and find properties of an item in it.

    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    @property
    def name(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        # print(item_link)
        item_name = item_link.attrs["title"]
        # print(item_name)
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocator.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        # print(item_link)
        item_href = item_link.attrs["href"]
        # print(item_href)
        return item_href

    @property
    def price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        price = self.soup.select_one(locator).string
        # print(price)
        # print(type(price))
        # price = float(price[1:])
        # print(price)
        # print(type(price))

        # using regex for price £51.77
        pattern = "£([0-9]+.[0-9]+)"
        matcher = re.search(pattern, price)
        print(matcher.group(0))
        print(matcher.group(1))
        print("type of the mathcher.group(1)", type(matcher.group(1)))
        print(float(matcher.group(1)))
        # 20 percent offer
        print(" 20 percent offer", float(matcher.group(1)) * 0.80)
        return float(matcher.group(1))

    @property
    def ratings(self):
        locator = ParsedItemLocator.RATINGS_LOCATOR
        rating_tag = self.soup.select_one(locator)
        rating_counts_classes = rating_tag.attrs["class"]
        print(rating_counts_classes)
        # using for loop
        rating_counts = [r for r in rating_counts_classes if r != "star-rating"]
        print(rating_counts[0])

        # # using lambda function
        # rating_counts = list(filter(lambda r: r != "star-rating", rating_counts_classes))
        # print(rating_counts)

        # # print(rating_counts_classes[1])
        # rating_counts = rating_counts_classes[1]
        # print(rating_counts)
        return rating_counts


# item = [PasedItem(p) for p in soup.find_all("article")]
item = PasedItem(ITEMLIST_HTML)
print(item.name)
# item.find_item_price()
# item.find_ratings()
