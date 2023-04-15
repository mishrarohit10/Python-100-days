import requests
import json
query = input("What type of news you want ? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-03-15&sortBy=publishedAt&apiKey=060e85448daa4eccab9d1f293a2c3ffc"
r = requests.get(url)
news = json.loads(r.text)
# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------")

