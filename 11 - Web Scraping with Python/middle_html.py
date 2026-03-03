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
soup = BeautifulSoup(ITEMLIST_HTML, "html.parser")
print("-" * 50)
print(soup)


def find_item_name():
    print("-" * 25, "find_item_name", "-" * 25)
    locator = "article.product_pod h3 a"
    item_link = soup.select_one(locator)
    print(item_link)
    item_name = item_link.attrs["title"]
    print(item_name)
    item_href = item_link.attrs["href"]
    print(item_href)


# find_item_name()


def find_item_price():
    print("-" * 25, "find_item_price", "-" * 25)
    locator = "article.product_pod p.price_color"
    price = soup.select_one(locator).string
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


find_item_price()


def find_ratings():
    print("-" * 25, "find_ratings", "-" * 25)
    locator = "article.product_pod p.star-rating"
    rating_tag = soup.select_one(locator)
    rating_counts_classes = rating_tag.attrs["class"]
    print(rating_counts_classes)
    # using for loop
    rating_counts = [r for r in rating_counts_classes if r != "star-rating"]
    print(rating_counts)

    # # using lambda function
    # rating_counts = list(filter(lambda r: r != "star-rating", rating_counts_classes))
    # print(rating_counts)

    # # print(rating_counts_classes[1])
    # rating_counts = rating_counts_classes[1]
    # print(rating_counts)


find_ratings()
