vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000,
                     'notebook dell': 17000, 'notebook asus': 2450}



#for val in vendas_tecnologia:
#     print(val, vendas_tecnologia[val])


aparelhos = []
valor = tot = 0
for I, J in vendas_tecnologia.items():
    if I[:8] == 'notebook':
        aparelhos.append(I)
        aparelhos.append(J)
        valor += J
for d in aparelhos:
    print(d)

print(f"\nToral em vendas: {valor}")




print(aparelhos[0: len(aparelhos)])
