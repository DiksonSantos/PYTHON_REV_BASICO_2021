
# vendas = []
logo = 'Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia'
vendas = []
flag = True

while flag:
    venda = str(input('Registre um produto: ').capitalize())

    if venda == '': # Se pressionar enter It Breaks
            flag = False
            break
    preco = input("Preço: ")
    vendas.append(venda)
    vendas.append(preco)
    # for j in vendas:


# print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))

#for R in vendas:
#    print(f"{R}, {R}")
print(vendas[0], vendas[1])
print(vendas)
# SOLUÇÃO DO PROFESSOR:
"""
venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
vendas = []
#crie aqui o programa

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')


print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))
"""
