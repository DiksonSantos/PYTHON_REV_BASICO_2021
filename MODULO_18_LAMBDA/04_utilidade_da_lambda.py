


preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}


def calcular_preco(preco):
    return preco * 1.3


preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values() ))

# Items, Key, values


# print(list(preco_com_imposto))


"""
for I in preco_com_imposto:
    print(f"Preço com impostos: {I}R$")
"""
# Lambda substitui DEFs simples (de um parametro)
preco_imposto_2 = list(map(lambda preco: preco * 1.3, preco_tecnologia.values()))
"""
for I in preco_imposto_2:
    print(f"Preço com impostos: {I}R$")
"""


# Usando 'Filter'  -> True ou False

def valor_maior(valor):
    return valor[1] > 2000


# Pegou do dicionario original -> Somente os produtos a cima de 2000R$
# print(dict(filter(valor_maior, preco_tecnologia.items())))

usando_lambda = dict(list(filter(lambda valor: valor[1] > 2000, preco_tecnologia.items())))

print(usando_lambda)
