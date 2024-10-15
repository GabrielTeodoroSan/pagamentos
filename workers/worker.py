import requests
from celery import Celery
from requests.auth import HTTPBasicAuth

from settings import Settings

app = Celery('tasks', broker=Settings().BROKER_URL)


def get_token():
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'client_credentials',
    }

    token = requests.post(
        Settings().ACCESS_TOKEN_URL,
        headers=headers,
        data=data,
        auth=HTTPBasicAuth(Settings().CLIENT_ID, Settings().SECRET_KEY),
    )

    return token.json()['access_token']


@app.task
def start_pay(products_info, user):
    ...
