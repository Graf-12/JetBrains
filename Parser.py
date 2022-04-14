import os
import string

import requests

from bs4 import BeautifulSoup

num_of_pages = int(input())
type_of_articles = input()
all_articles_dict = {}
i = 1
res = [" ", ":", ",", "__", "___", "—", "-", "’", "‘"]

while True:
    if num_of_pages == 0:
        break
    else:
        try:
            os.mkdir(f"Page_{i}")
        except FileExistsError:
            pass
        url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page={i}"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        news = soup.find_all(class_="app-article-list-row__item")
        for type_ in news:
            articles_type = type_.find(class_="c-meta__type")
            if articles_type.text == type_of_articles:
                href = type_.find(class_="c-card__link u-link-inherit")
                item_name = href.text
                item_href = "https://www.nature.com" + href.get('href')
                for sign in res:
                    if sign in item_name:
                        name = item_name.replace(sign, "_").replace("___", "_").strip(string.punctuation)
                req = requests.get(url=item_href)
                soup = BeautifulSoup(req.content, "html.parser")
                content = soup.find(class_="c-article-body")
                with open(f"Page_{i}/{name}.txt", "w") as file:
                    text = content.text.strip()
                    file.write(text)
        num_of_pages -= 1
        i += 1
print("Done")
