import datetime
import webbrowser
from modules.news import get_top_news
from modules.speaker import speak
from modules import weather,listener
from modules.briefinfo import get_summary

site_urls = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "wikipedia": "https://www.wikipedia.org"
}

def handle_command(command):
    response = ""

    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The time is {now}"

    
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        response = f"Today is {today}"

    elif "weather" in command and "current" in command:
        report = weather.get_weather_in_current_location()
        response = report

    elif "news" in command or "headlines" in command:
     response = get_top_news()


    elif any(phrase in command for phrase in ["tell me about", "what is", "who is"]):
        topic = command
        for phrase in ["tell me about", "what is", "who is"]:
            if phrase in topic:
                topic = topic.replace(phrase, "")
                break
        topic = topic.strip()
        if topic:
            response = get_summary(topic)
        else:
            response = "Please specify a topic to look up."

    elif any(phrase in command for phrase in ["open", "go to"]):
        found = False
        for keyword, url in site_urls.items():
            if keyword in command:
                webbrowser.open(url)
                response = f"Opening {keyword.capitalize()}"
                found = True
                break

        if not found:
            search_term = command.replace("open", "").replace("go to", "").strip()
            if search_term:
                search_url = f"https://www.google.com/search?q={search_term}"
                webbrowser.open(search_url)
                response = f"I couldn't find a direct site for '{search_term}', so I searched it on Google."
            else:
                response = "Please tell me what to open."

    else:
        response = "I didn't understand the command."

    speak(response)
    return response
