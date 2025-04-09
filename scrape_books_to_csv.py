import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Set up the URL and headers
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Find all book entries
books = soup.find_all("article", class_="product_pod")

# Step 3: Prepare the CSV file
with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)   
    writer.writerow(["Title", "Price", "Availability"])

# Step 4: Loop through and write data
    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        writer.writerow([title, price, availability])