from pydantic import BaseModel


class ProductsInfo(BaseModel):
    products: list[str]
    price_total: float


class PurchaseInfo(BaseModel):
    user_name: str
    user_id: int
    products: list[str]


class User(BaseModel):
    id: int 
    name: str
    