import time
from discordwebhook import Discord
from bs4 import BeautifulSoup
import requests

def site(link,webhook_url):
    https = link
    discord = Discord(url=webhook_url)
    site1 = requests.get(https)
    sayfa_icerik = site1.content
    soup = BeautifulSoup(sayfa_icerik, "html.parser")
    for i in soup.find_all("div", {"class": "product-button-container"}):
        if i.text == "Sepete EkleSepete EklendiFavorilere Ekle":
            discord.post(content="Stok Vardır.")
            exit()
        else:
            discord.post(content="Stok Yoktur.")
sit = input("Site Linki :")
webhook = input("Webhook Url Linki :")
while True:
    time.sleep(3)
    site(sit,webhook)



