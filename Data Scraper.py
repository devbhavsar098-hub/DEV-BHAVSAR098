import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

with open("headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])

    for title in titles:
        writer.writerow([title.text])

print("Data saved to headlines.csv")
