


# lista = [expressão for item in iterable if condição]

meta = 1000
vendas_prod = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']


prod_upper_meta = [produto for i, produto in enumerate(produtos) if vendas_prod[i] > meta]
print(', '.join(prod_upper_meta))
