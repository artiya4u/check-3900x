import requests

from notification import notify


def check_jib():
    url = "https://www.jib.co.th/web/product/product_list/3/1237"

    payload = ""
    headers = {'Cache-Control': 'no-cache'}
    response = requests.request("GET", url, data=payload, headers=headers)

    if response.text.find('3900X') != -1:
        notify('Ryzen9 3900x เข้าแล้ว', 'กดเลยที่ ' + url)
    else:
        print("Not found in JIB")


if __name__ == '__main__':
    check_jib()
