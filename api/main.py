from fastapi import FastAPI

from api.schemas import ProductsInfo, PurchaseInfo, User
from workers.worker import start_pay

app = FastAPI()


@app.post('/pay/')
async def pay(products_info: ProductsInfo, user: User) -> str:
    result = await start_pay(products_info, user)
    links = result.json()['links']
    return next(l['href'] for l in links if l['rel'] == 'payer-action')
