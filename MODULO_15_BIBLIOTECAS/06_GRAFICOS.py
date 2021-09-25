import matplotlib.pyplot as plt

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

#plotar o gráfico da forma mais simples

# Eixos X, Y
plt.plot(meses, vendas_meses) # , 'ro'   -> Dentro das ()  == Graf Bolinhas
plt.ylabel('Preço')
plt.xlabel('Meses')

# A ideia é boa, e, funcionou :0
plt.axis([meses[0], meses[-1], min(vendas_meses), max(vendas_meses)+500])


# Ok It works well:
# plt.axis([0, 12, 0, 2762])

plt.show()
