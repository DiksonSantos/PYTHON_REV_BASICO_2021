# METODOS PARA JUNTAR LISTAS:

vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# for I, J in enumerate(vendas_produtos):
#    print(produtos[I], J)


for I, J in enumerate(produtos):
    arruma = vendas_produtos[I]
    # print(vendas_produtos[I], J)





zipado = list(zip(vendas_produtos, produtos))
# zipado = zip(vendas_produtos, produtos)
# print(list(zipado))
# print(dict(zip(produtos, vendas_produtos)))

# print(zipado.sort())
zipado.sort(reverse=True)
# print(type(zipado))


# UNPACKING LISTA:
# Var = chave for valor , Mostrar_Chave IN Lista
# print filtro == Chaves Da Lista
produtos = [produto for vendas, produto in zipado]
print(produtos)
