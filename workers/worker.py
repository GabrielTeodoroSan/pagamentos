import json
import uuid

import requests
from requests.auth import HTTPBasicAuth

from settings import Settings


async def get_token() -> str:
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


async def start_pay(products_info, user):
    access_token = await get_token()

    data = {
        'intent': 'CAPTURE',
        'purchase_units': [
            {
                'reference_id': f'{uuid.uuid4()}',
                'amount': {
                    'currency_code': 'BRL',
                    'value': f'{products_info.price_total}',
                },
            }
        ],
        'payment_source': {
            'paypal': {
                'experience_context': {
                    'payment_method_preference': 'IMMEDIATE_PAYMENT_REQUIRED',
                    'brand_name': 'EXAMPLE INC',
                    'locale': 'pt-BR',
                    'landing_page': 'LOGIN',
                    'shipping_preference': 'NO_SHIPPING',
                    'user_action': 'PAY_NOW',
                    'return_url': f'{Settings().API_BASE_URL}return',
                    'cancel_url': f'{Settings().API_BASE_URL}cancel',
                }
            }
        },
    }

    header = {
        'Content-Type': 'application/json',
        'PayPal-Request-Id': f'{uuid.uuid4()}',
        'Authorization': f'Bearer {access_token}',
    }

    order_response = requests.post(
        Settings().BASE_ORDER_URL, headers=header, data=json.dumps(data)
    )

    if order_response.status_code == 200:
        return order_response
    else:
        return {
            'message': f'Erro {order_response.status_code} // {order_response.text}'
        }
