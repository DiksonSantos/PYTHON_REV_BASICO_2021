vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for produto, vendas_19, vendas_20 in vendas_produtos:
    # Para saber do crescimento de 2020 em relação a 19, devemos buscar somente os valores de 2020 que foram maiores que 19
    if vendas_20 > vendas_19:
        # Então dividimos estes valores Maiores de 2020 pelos Menores de 2019:
        print(f"Produto {produto} Vendas em 2019: {vendas_19} vendas em 2020 {vendas_20} \n % De Crescimento: {(vendas_20 / vendas_19 - 1):.1%}")
