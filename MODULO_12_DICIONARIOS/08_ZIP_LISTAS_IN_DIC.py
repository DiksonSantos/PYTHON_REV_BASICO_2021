# produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
# vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

# novo = dict(zip(produtos, vendas))

# print(novo)

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell',
            'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467,
              489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633,
              725316, 644622, 994303]

"""
# MEU METODO -> WRONG:
Pro_Ven_19 = dict(zip(produtos, vendas2019))
Pro_Ven_20 = dict(zip(produtos, vendas2020))
Pro_Ven_19.update(Pro_Ven_20)
print(Pro_Ven_19)
"""


# METODO DO PROFESSOR:
vendas = list(zip(vendas2019, vendas2020))
vendas_produtos = dict(zip(produtos, vendas))
print(vendas_produtos)
