from workers.worker import get_token


async def test_if_token_are_generated():
    token = await get_token()
    assert type(token) == str
    assert len(token) > 0
