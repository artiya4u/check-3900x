import requests

TOKEN = "YOUR TOKEN"


def notify(title, message):
    url = "https://notify-api.line.me/api/notify"

    payload = {"message": "{}\n {}".format(title, message)}
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': "Bearer {}".format(TOKEN)
    }

    response = requests.request("POST", url, data=payload, headers=headers)
