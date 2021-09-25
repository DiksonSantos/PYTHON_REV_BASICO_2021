
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
prod = 'coca'


def padroniza(texto):
    texto = texto.upper()
    return texto

# DESTA FORMA NÃO FUNCIONA -> .UPPER() NÃO FUNCIONA COM LISTAS:
# for i, produto in enumerate(produtos):
#     produto[i] = padroniza(produtos)
#print(produtos)


# DESTA FORMA FUNCIONA:
lista = list(map(padroniza, produtos))
print(lista)
