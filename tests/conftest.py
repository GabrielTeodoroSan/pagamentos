from random import randint

import factory
import pytest
from faker import Faker

from api import schemas

fake = Faker()


class User(factory.Factory):
    class Meta:
        model = schemas.User

    id = randint(0, 1000)
    name = fake.name()


class ProductsInfo(factory.Factory):
    class Meta:
        model = schemas.ProductsInfo

    products = [fake.company() for i in range(3)]
    price_total = randint(0, 1000)


@pytest.fixture
def user():
    yield User()


@pytest.fixture
def products_info():
    yield ProductsInfo()
