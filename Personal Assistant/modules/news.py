
import requests
from bs4 import BeautifulSoup

def get_top_news():
    try:
        url = "https://www.ndtv.com/latest?pfrom=home-ndtv_mainnavigation"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return "Sorry, I couldn't fetch the news right now."

        soup = BeautifulSoup(response.content, "html.parser")
        news_cards = soup.find_all("div", class_="news-card", limit=5)

        headlines = []
        for card in news_cards:
            title_span = card.find("span", itemprop="headline")
            if title_span:
                headlines.append(title_span.text.strip())

        if headlines:
            return "Here are the top headlines: " + " ... ".join(headlines)
        else:
            return "No headlines found at the moment."

    except Exception as e:
        print(f"[ERROR scraping news] {e}")
        return "Sorry, there was a problem fetching the news."
