import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Safety-1st-Grow-Convertible-Carbon/dp/B07HB1TQXP?pd_rd_w=ZFZXS&pf_rd_p=43ea9b7e-4160-4f68-b311-3810df065596&pf_rd_r=86QGRY9BDK1GPWNEF3XA&pd_rd_r=6ca81f54-1bac-4303-be93-0ffaa7807d73&pd_rd_wg=6FvBf"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
PRICE_VALUE = 140
EMAIL_ADDRESS = "adamas242@gmail.com"

def trackPrices():
    price = float(getPrice())
    if price > PRICE_VALUE:
        diff = int(price - PRICE_VALUE)
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper! Notifying...")
        sendEmail()
    pass

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()[1:4]
    print(title)
    print(price)
    return price

def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'wazLincsLuna18!')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    pass

if __name__ == "__main__":
    trackPrices()
