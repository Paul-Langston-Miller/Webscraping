from bs4 import BeautifulSoup
import requests
import time

html_text_chelsea = requests.get('https://www.football.london/chelsea-fc/transfer-news/').text
soup_chelsea = BeautifulSoup(html_text_chelsea, 'lxml')
chelsea_news_text = soup_chelsea.find_all('div', class_= "teaser-text")
for c in chelsea_news_text:
    print(c.text)
chelsea_links = soup_chelsea.find_all('a', class_ = "headline")
for link in chelsea_links:
    print(link['href'])

