"""
soma = []
for I in range(0, 11):
    xorg = I

    print(f"{xorg}", end=' ')

soma.append(xorg)
print("\n", soma[:])
"""

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

for I in range(len(produtos)):
    print(produtos[I].capitalize(), producao[I], " Unidade Produzidas")


# for produto in produtos:
#    print(produto)

# SOMA CADA UM DOS ITENS/PREÇOS NA LISTA:
# Variavel auxiliar
soma = 0
for prod in producao:
    soma += prod
print(f"Total em Vendas: {soma}")

vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000
