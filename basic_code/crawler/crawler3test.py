import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"

}

for index in range(0,250,25):
    response = requests.get("https://movie.douban.com/top250", headers=headers)
    html = response.text

    print(response.ok)

    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.find_all("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)

