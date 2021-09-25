import matplotlib.pyplot as plt
import numpy as np
# Variavel Random-Nums_Aleatorios Randint-Gera-Numero_Inteiro | Min, Max, Quantidade de Numeros-Gerados
vendas = np.random.randint(1000, 3000, 50)


# Gera de 1 a 50
meses = np.arange(1, 51)
# print(meses)

# print(vendas, '\n')
# print('Maior_Valor:', max(vendas), 'Menor Valor: ', min(vendas), 'Quantidade: ', len(vendas))
"""
mes = ''
sel = 0
for I, J in enumerate(meses):
    # print('Venda: ', vendas[I], 'Mês:', J)
    sel = vendas[I]
    mes = J
"""


plt.axis([meses[0], meses[-1], min(vendas), max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')

# Bolinhas:
# plt.plot(meses, vendas, 'ro')

# Linha Normal:
# plt.plot(meses, vendas)

# nha cor verde
# plt.plot(meses, vendas, 'g')

# Triangulos:
# plt.plot(meses, vendas, 'g^')

# Tracejado:
# plt.plot(meses, vendas, 'r--')

# Blue:
# plt.plot(meses, vendas, 'b')

# Bolinhas:
# plt.scatter(meses, vendas)

# Barras:
# plt.bar(meses, vendas)

#plt.show()

# SUBPLOTs
# plt.subplot(131)
# plt.bar(meses, vendas)
# plt.show()


# Quantidade de gráficos (Teoricament) define tamanho da figura:
plt.figure(1, figsize=(19, 3))
# Linhas ,Colunas, posição do gráfico (De gráficos):
plt.subplot(1, 3, 1)
# Quem vai ser o gráfico na posição 1 :
plt.plot(meses, vendas, 'b')


plt.subplot(1, 3, 2)
# Quem vai ser o gráfico na posição 2 :
plt.plot(meses, vendas, 'g^')


plt.subplot(1, 3, 3)
# Quem vai ser o gráfico na posição 3 :
plt.plot(meses, vendas, 'r--')

plt.show()
