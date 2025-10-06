produtos = [
    {'nome': 'goiaba', 'quantidade': 10, 'valor': 100},
    {'nome': 'maçã', 'quantidade': 5, 'valor': 40},
    {'nome': 'pera', 'quantidade': 3, 'valor': 20},
    {'nome': 'uva', 'quantidade': 0, 'valor': 90},
    {'nome': 'banana', 'quantidade': 1, 'valor': 50},
]
#Dicionário com com os produts , quantidade e valores 
def controle_estoque(produtos):
    print("\n Controle de Estoque ")
    for i in range(len(produtos)):
        nome = produtos[i]['nome']
        qtd = produtos[i]['quantidade']
        if qtd == 0:
            print(f"{nome or 'Produto sem nome'}: Fazer pedido urgente!")
        elif qtd <= 3:
            print(f"{nome or 'Produto sem nome'}: Alerta! Estoque baixo ({qtd} unidades)")
        else:
            print(f"{nome or 'Produto sem nome'}: Ok ({qtd} unidades)")


def compra(produtos):
    print("\n Análise de Preços ")
    produtos_mais_caro = produtos[0]
    for i in range(1, len(produtos)):
        if produtos[i]['valor'] > produtos_mais_caro['valor']:
            produtos_mais_caro = produtos[i]
    nome = produtos_mais_caro['nome']
    valor = produtos_mais_caro['valor']
    print(f"O produto mais caro é {nome} (R${valor:.2f})")

    produtos_mais_barato = produtos[0]
    for i in range(1, len(produtos)):
        if produtos[i]['valor'] < produtos_mais_barato['valor']:
            produtos_mais_barato = produtos[i]
    nome = produtos_mais_barato['nome']
    valor = produtos_mais_barato['valor']
    print(f"O produto mais barato é {nome} (R${valor:.2f})")


def faturamento(produtos):
    print("\n Simulação de Vendas e Faturamento ")
    vendas = []
    total_faturado = 0

    while True:
        nome = input("Digite o nome do produto vendido (ou 'sair' para encerrar): ").lower()
        if nome == 'sair':
            break

        encontrado = False
        for i in produtos:
            if i['nome'].lower() == nome:
                encontrado = True
                qtd_vendida = int(input(f"Quantidade vendida de {nome}: "))

                if qtd_vendida > i['quantidade']:
                    print("Estoque insuficiente!")
                else:
                    i['quantidade'] -= qtd_vendida
                    valor_venda = qtd_vendida * i['valor']
                    total_faturado += valor_venda
                    vendas.append({'produto': nome, 'quantidade': qtd_vendida, 'valor': valor_venda})
                    print(f"Venda registrada: {nome} x{qtd_vendida} = R${valor_venda:.2f}")
                break

        if not encontrado:
            print("Produto não encontrado.")

    # Relatório final no console
    print("\n Relatório Final")
    print("Lista de produtos e quantidades finais no estoque:")
    for i in produtos:
        print(f"{i['nome'] or 'Produto sem nome'} - {i['quantidade']} unidades (R${i['valor']:.2f})")

    acima_100 = [i for i in produtos if i['valor'] > 100]
    print(f"\nProdutos com valor acima de R$100: {len(acima_100)}")

    from datetime import datetime #o datetima é para mostar o dia/mês/ano e o Horário
    data_relatorio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Faturamento total do dia: R${total_faturado:.2f}")
    print(f"Data de geração do relatório: {data_relatorio}")


# Execução principal
controle_estoque(produtos)
compra(produtos)

faturamento(produtos)
