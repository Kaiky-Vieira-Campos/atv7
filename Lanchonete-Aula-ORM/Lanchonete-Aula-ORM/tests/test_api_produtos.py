async def test_get_produto_inexistente(client):
    response = await client.get("/produtos/9999")
    assert response.status_code == 404


async def test_alterar_valor_produto(client):
    response = await client.post(
        "/produtos",
        json={"codigo": 1, "valor": 10.0, "tipo": 1, "desconto_percentual": 10.0},
    )
    assert response.status_code == 200

    response2 = await client.put(
        "/produtos/1/valor",
        json={"novo_valor": 15.0},
    )
    assert response2.status_code == 200
    assert response2.json() == {"alterou": True}
