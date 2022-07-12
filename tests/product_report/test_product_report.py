from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "caneca",
        "Schimidt",
        "2022-06-12",
        "indeterminada",
        "1234",
        "Cuidado frágil",
    )

    assert str(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
