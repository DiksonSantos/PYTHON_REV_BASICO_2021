preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']


def calcular_imposto(preco, imposto):
    '''Metodo Tradicional'''
    return preco * imposto


# Metodo List Comprehension:
impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)
print(impostos)

# Usando a Fun DEF dentro de uma ListComprehension:
calcula = [calcular_imposto(preco, 0.3) for preco in preco_produtos]

