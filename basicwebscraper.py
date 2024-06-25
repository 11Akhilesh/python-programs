import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('a', class_='storylink')
for i, title in enumerate(titles, 1):
    print(f"{i}. {title.text}")
