# lista.sort()   -> Altera a ordem da lista
# sorted(lsta) -> Retorna valores em outra ordem

produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull']


lista_nova = sorted(produtos)
# print(lista_nova)

# for I in lista_nova:
#     print(I)


# produtos.sort()
# print(produtos)


vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900}

vendedores_lista = vendedores_dic.items()

#for I, J in vendedores_lista:
#    print(J)

def segundo_item(tupla):
    return tupla[1]


lista_vendas = list(vendedores_dic.items())
# .sort() -> Usa como padrão pegar o primeiro item para por em ordem. Mas mudamos a regra usando o key=
#.. e usando a função para isso.
lista_vendas.sort(key=segundo_item) # pode usar ', reverse=True'  para inverter a ordem.
print(lista_vendas)

# Voltando p/ Dict, porém desta vez ordenado:
print(dict(lista_vendas))

