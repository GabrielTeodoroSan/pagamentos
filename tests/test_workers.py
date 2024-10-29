from workers.worker import start_pay


async def test_if_start_pay_is_working(user, products_info):
    response = await start_pay(products_info, user)
    assert type(response) == str
    assert len(response) > 0
