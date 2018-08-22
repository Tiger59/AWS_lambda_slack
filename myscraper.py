import requests
import slackweb
from bs4 import BeautifulSoup


def scraping_handler(event, context):
    r = requests.get("https://news.yahoo.co.jp/")
    soup = BeautifulSoup(r.content, "html.parser")
    slack = slackweb.Slack(url="INCOMING WEBHOOKS API KEY ")

    remove_words=["写真","new"]
    for i in soup.select("p.ttl"):
        topic = i.getText()
        for str in remove_words:
            topic = topic.replace(str,"")
        slack.notify(text=topic)