meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

atingiram = []
quantos = 0
x = 0
vendors = []

for I, j in vendas:
    if j > meta:
        atingiram.append(j)
        quantos += 1
        x = quantos / len(vendas)
        vendors.append(I)


print(f"Porcentagem de  Vendedores que atingiram a meta: {x:.1%} Deles\n"
      f"Totalizando {quantos} Vendedores")

mostrar = ''
for G in vendors:
    # print(f"Respectivamente\n{G}")
    mostrar += str(G) + ','
    print(G, end='  ')

# print(mostrar.split(','))

# SOLUÇÃO DO PROFESSOR (MAIS SUCINTA)
"""
#seu código aqui
melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]
        
print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendedor, maior_vendas))
"""
