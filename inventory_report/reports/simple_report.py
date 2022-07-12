from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, produtos):
        datas_de_fabricacao = list()
        for produto in produtos:
            datas_de_fabricacao.append(produto["data_de_fabricacao"])

        datas_de_validade = list()
        for produto in produtos:
            datas_de_validade.append(produto["data_de_validade"])

        empresas = list()
        for produto in produtos:
            empresas.append(produto["nome_da_empresa"])
        maior_vendedora = Counter(empresas).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(datas_de_fabricacao)}\n"
            f"Data de validade mais próxima: {min(datas_de_validade)}\n"
            f"Empresa com mais produtos: {maior_vendedora}"
        )
