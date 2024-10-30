async def test_se_a_api_esta_funcionando_corretamente(
    client, user, products_info
):
    response = client.post('/pay/', user, product)
    assert response.status_code == 200
    assert isinstance(response.text, str)
