from workers.worker import start_pay


async def test_if_start_pay_is_working(celery_app, celery_worker, user, products_info):
    response = await start_pay.apply_sync(products_info, user)
    assert type(response.get()) == str
    assert len(response.get()) > 0
