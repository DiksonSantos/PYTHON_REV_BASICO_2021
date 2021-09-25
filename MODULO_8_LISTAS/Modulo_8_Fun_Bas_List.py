produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

print(len(produtos))


vendas = [1000, 1500, 15000, 270, 900, 100, 1200]

maximo_v = max(vendas)
minima_venda = min(vendas)
print(maximo_v, minima_venda)

print("Produto mais & Menos Vendido")
print("Mais Indice: ", vendas.index(maximo_v))
print("Menos Indice: ", vendas.index(minima_venda))

Mais = vendas.index(maximo_v)
Prod_Mais = produtos[Mais]
Menos = vendas.index(minima_venda)
Prod_Menos = produtos[Menos]

print(f'Mais Vendido {Prod_Mais.upper()}')
print(f'Prod Menos Vendido {Prod_Menos.upper()}')
