from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "caneca",
        "Schimidt",
        "2022-06-12",
        "indeterminada",
        "1234",
        "Cuidado frágil",
    )

    assert product.id == 1
    assert product.nome_do_produto == "caneca"
    assert product.nome_da_empresa == "Schimidt"
    assert product.data_de_fabricacao == "2022-06-12"
    assert product.data_de_validade == "indeterminada"
    assert product.numero_de_serie == "1234"
    assert product.instrucoes_de_armazenamento == "Cuidado frágil"
