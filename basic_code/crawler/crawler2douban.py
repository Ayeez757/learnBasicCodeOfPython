import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}
response = requests.get("https://books.toscrape.com/",headers=headers)
print(response.status_code)
content = response.text
soup = BeautifulSoup(content,"html.parser")
all_prices=soup.findAll("p",attrs={"class":"price_color"})
for price in all_prices:
    print(price.string)