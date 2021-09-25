mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}


# Pegando informações:
print(mais_vendidos.get('refrigeracao'))
print(mais_vendidos['refrigeracao'])


"""
Se digitar o nome errado usando o metodo GET ele apenas retorna 'none' , já se usar chaves ele 
da um erro. (se digitar o nome errado).
"""


# Verificando Se uma chave existe:
if 'canela' in vendas_tecnologia:
    print(vendas_tecnologia['canela'])
else:
    print('Não encontrado')

# COM O OUTRO METODO:
if vendas_tecnologia.get('copo') == None:
    print('Não encontrado')
