
# Representam os 4 vendedores / 4 Linhas em vendas (capitch?)
vendedores = ['Lira',
              'João',
              'Diego',
              'Alon']

# Representam os Itens de venda 0 & 1
produtos = ['ipad', 'iphone']

vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

# LINHA X ITEM:

# Item 1 da Linha 0 -> 200
print(vendas[0][1])

# Sempre Indice 1
venda_iphones = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print("Total:", venda_iphones, "Iphones Vendidos\n"
                     "vendedor -> ", vendedores[0], "Vendas", vendas[0][1])

# modificando comprecisão:

# De 200 Para 50 :   Valor 1 Da  Linha Zero
vendas[0][1] = 50
print(vendas)


vendas_mac = [10, 15, 6, 70]

# LINHAS X ITENS DE 'vendas_mac'  :
vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])

for I in vendas:
    print(I)
