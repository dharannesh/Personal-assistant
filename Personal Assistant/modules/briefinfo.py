import requests
from bs4 import BeautifulSoup

def get_summary(topic):
    try:
        search_topic = topic.strip().replace(" ", "_")
        url = f"https://en.wikipedia.org/wiki/{search_topic}"
        response = requests.get(url)

        if response.status_code != 200:
            return "Sorry, I couldn't find information about that."

        soup = BeautifulSoup(response.text, "html.parser")
       
        paragraphs = soup.find_all("p")
        for para in paragraphs:
            if para.text.strip():
                return para.text.strip()

        return "Sorry, I couldn't extract a summary."
    except Exception as e:
        return f"Error: {str(e)}"
