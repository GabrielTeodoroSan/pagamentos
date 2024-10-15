from fastapi import Fastapi
from api.schemas import User, ProductsInfo, PurchaseInfo


app = Fastapi()


@app.post('/pay/')
def pay(products_info: ProductsInfo, user: User):
    result = payment.delay(products_info, user)
    return result