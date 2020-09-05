import requests
import json


def speak(str):
    from win32com.client import Dispatch
    tell = Dispatch("SAPI.spvoice")
    tell.speak(str)


if __name__ == "__main__":
    speak("good morning")
    url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-03&sortBy=publishedAt&apiKey=e684369eea9446d19026cf7281f207c9"
    news = requests.get(url).text
    latest_news = json.loads(news)
    news_reader = latest_news["articles"]
    for articles in news_reader:

        speak("today's latest news are")
        print("\t\t**Today Latest News**\t\t")
        speak(articles['title'])
        print("News:- ", articles['title'])
        speak("Moving on to the next news..Listen Carefully")

speak("thank you for listening")
print("\t\tThank you for listening..")
