vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

vendas_19 = []
pro_19 = []

for I in vendas_produtos:
    # print(I[1])
    vendas_19.append(I[1])
    pro_19.append(I[0])
    # print(vendas_19)

#print(pro_19)
#print(vendas_19)
maior = []
for g, h in enumerate(pro_19):
    produto = str(h)
    # print('Produro_2019: ', produto.upper(), 'Faturamento:', vendas_19[g])
    maior.append(vendas_19[1])


print('Maior Venda/Valor:', max(maior))



# Só o faturamento de 2019
comprehension = [I[1] for I in vendas_produtos]
print(comprehension)
