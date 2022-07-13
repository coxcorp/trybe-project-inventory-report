from collections import Counter


class CompleteReport:
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
        empresas_quantificadas = Counter(empresas).most_common()
        maior_vendedora = empresas_quantificadas[0][0]

        produtos_empresa = ""
        for empresa in empresas_quantificadas:
            produtos_empresa += f"- {empresa[0]}: {empresa[1]}\n"

        return (
            f"Data de fabricação mais antiga: {min(datas_de_fabricacao)}\n"
            f"Data de validade mais próxima: {min(datas_de_validade)}\n"
            f"Empresa com mais produtos: {maior_vendedora}\n"
            "Produtos estocados por empresa:\n"
            f"{produtos_empresa}"
        )
