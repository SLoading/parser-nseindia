import requests
from bs4 import BeautifulSoup

response = requests.get('https://x.com/elonmusk')
response.raise_for_status()  # Проверка на ошибки HTTP

soup = BeautifulSoup(response.content, 'html.parser')
tweets = soup.find_all('div', class_='css-175oi2r')

# Выбираем только 10 последних твитов
tweets = tweets[:10]

# Извлекаем текст каждого твита
if tweets:
    for tweet in tweets:
        tweet_text = tweet.xpath("//div[@class='css-175oi2r']")
        if tweet_text:
           print(tweet_text.text.strip())
else:
    print("Получить данные не вышло")
