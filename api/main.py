from fastapi import FastAPI

from api.schemas import Link, ProductsInfo, PurchaseInfo, User
from workers.worker import start_pay

app = FastAPI()


@app.post('/pay/')
async def pay(products_info: ProductsInfo, user: User) -> Link:
    result = await start_pay(products_info, user)
    links = result.json()['links']
    return {
        'link': next(l['href'] for l in links if l['rel'] == 'payer-action')
    }
