import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the live website
url = "https://books.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all book containers
books = soup.find_all("article", class_="product_pod")

# Step 4: Loop through and print title and price
for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text
    print(f"{title} - {price}")