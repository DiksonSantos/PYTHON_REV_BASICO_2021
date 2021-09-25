

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

# PRODUTO MAIS VENDIDO (EM UNIDADES) NO DIA 20/08/2020
mais_vendido = color = data = cap = ''
qtd_prod_mais_vend = val_UN = 0
for item in vendas:
    # Itens a serem Desempacotados e Percorridos:
    data, produto, cor, capacidade, unidades, valor_unitario, = item
    if data == '20/08/2020':
        if unidades > qtd_prod_mais_vend:
            mais_vendido = produto
            qtd_prod_mais_vend = unidades
            val_UN = valor_unitario
            color = cor
            cap = capacidade
print(f"Data: {data} \nProduto: {mais_vendido} \nCor: {color} \nCapacidadeGB: {cap} \n"
      f"Quantidade: {qtd_prod_mais_vend} \nValor_Unit: {val_UN}")
