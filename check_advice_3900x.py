from bs4 import BeautifulSoup
import requests

from notification import notify


def check_advice():
    url = "https://www.advice.co.th/product/cpu/amd-am4/cpu-amd-am4-ryzen9-3900x"

    payload = ""
    headers = {'Cache-Control': 'no-cache'}
    response = requests.request("GET", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find("div", {"class": "btn"})
    if "Arriving (1-3 days)" != price.text.strip():
        notify('Ryzen9 3900x เข้าแล้ว', 'กดเลยที่ ' + url)
    else:
        print("Not found in ADVICE")


if __name__ == '__main__':
    check_advice()
