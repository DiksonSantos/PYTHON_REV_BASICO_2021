

# String (Mais facil de digitar)
meses = 'jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez'

# Transformei numa Lista:
months = meses.split(',')
# print(months)


vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# Juntar Listas:
vendas_1sem.extend(vendas_2sem)
vendas_1sem.sort(reverse=False)

maximo = max(vendas_1sem)
minimo = min(vendas_1sem)
# print(f"Maior Venda: {maximo}")

indexo = vendas_1sem.index(maximo)

# print("Mês de maior Faturamento:", months[indexo])

res = dict(zip(months, vendas_1sem))
# print(type(res))

# print(res)
for I, J in res.items():
    if J == maximo:
        print(f"Mês: {I}, Maior Venda: {J}")

print('\n')

for I, J in res.items():
    if J == minimo:
        print(f"Mês -> {I}, Menor Venda do Ano: {J}")

soma = sum(vendas_1sem)
print(f"Total Anual de Vendas R${soma:.2f}")

percentual = maximo / soma
print(f"Percentual Anual {percentual:.1%}")

# Top 3 maiores Vendas do Ano:
maior = maximo
top1 = max(vendas_1sem)
# print(top1)
vendas_1sem.remove(maior)
top2 = max(vendas_1sem)
# print(top2)
# print(max(vendas_1sem))
cp = vendas_1sem.copy()
cp.remove(max(cp))
top3 = max(cp)


print(f"Top 3 Maiores vendas do Ano: "
      f"\nPrimeira:{top1:.2f} R$\n"
      f"Segunda: {top2:.2f} R$\n"
      f"Terceira: {top3:.2f} R$")
