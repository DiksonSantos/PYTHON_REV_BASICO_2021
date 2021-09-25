vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# SUBSTITUIMOS OS NOMES DOS ITENS DA CHAVE DA TUPLA POR NOMES MAIS INTUITIVOS:
# DESEMPACOTANDO SOMENTE A LINHA 0 DA TUPLA:
# x = data, produto, cor, capacidade, qtd_vendidos, valor_unidade = vendas[0]

# print(x)
# faturamento = qtd_vendidos * valor_unidade
# upper_cut = str(produto)
# print(F' {upper_cut.upper()} Faturamento {faturamento}')

x = ''
faturamento = 0
datass = ''
for item in vendas:
    data, produto, cor, capacidade, unidades, preco = item
    if produto == 'iphone x' and data == '20/08/2020':
        # print(produto)
        x = produto
        datass = data
        faturamento += unidades * preco

print(f"Total de vendas de {x.upper()} no dia: {datass} foi de: {faturamento:,} R$")


# OUTRA SOLUÇÃO:
"""
x = ''
faturamento = 0
datass = ''
# Outra forma de fazer o UnPack:
for data, produto, cor, capacidade, unidades, preco in vendas:
    if produto == 'iphone x' and data == '20/08/2020':
        # print(produto)
        x = produto
        datass = data
        faturamento += unidades * preco

print(f"Total de vendas de {x.upper()} no dia: {datass} foi de: {faturamento:,} R$")
"""
