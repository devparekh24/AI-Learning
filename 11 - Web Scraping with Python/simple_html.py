from bs4 import BeautifulSoup

SIMPLE_HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Document</title>
</head>
<body>
  <h1>This is the title2</h1>
  <h1>This is the title1</h1>
  <p class="subtitle">This is a paragraph</p>
  <p>Here is the second paragraph without a class</p>
  <p>Here is the third paragraph without a class</p>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</body>
</html>"""

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")

print("-" * 50)
print(simple_soup.find("h1"))
print("-" * 50)
print(simple_soup.find("h1").string)
print("-" * 50)
print(simple_soup.find("h1").text.strip())
print("-" * 50)
print(simple_soup.prettify())


def find_h1_title():
    print("-" * 50)
    print(simple_soup.find("h1").string)


find_h1_title()


def find_list_items():
    print("-" * 50)
    lists = simple_soup.find_all("li")
    print(lists)
    print("-" * 50)
    for l in lists:
        print(l.string)
    print("-" * 50)
    list_items = [l.string for l in lists]
    print(list_items)


find_list_items()


def find_subtitle():
    print("-" * 50)
    subtitle = simple_soup.find("p", class_="subtitle")
    print(subtitle.string)
    print("-" * 50)
    paragraph = simple_soup.find("p", {"class": "subtitle"})
    print(paragraph)
    print("-" * 50)
    print(paragraph.string)


find_subtitle()


def find_other_paragraph_without_class_name():
    print("-" * 50)
    print("find_other_paragraph_without_class_name")
    all_paragrphs = simple_soup.find_all("p")
    other_paras = [
        p for p in all_paragrphs if "subtitle" not in p.attrs.get("class", [])
    ]
    print(other_paras)
    print("-" * 50)
    print(other_paras[0].string)
    print(other_paras[1].string)
    print("-" * 50)
    list_all_other_parags = [l.string for l in other_paras]
    print(list_all_other_parags)


find_other_paragraph_without_class_name()
