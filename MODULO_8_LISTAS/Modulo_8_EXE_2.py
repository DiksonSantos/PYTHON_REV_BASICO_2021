
produtos = ['computador', 'livro', 'tablet', 'celular', 'tv',
            'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

# A posição de 'livro' em Produtos é 1
# print(produtos.index('livro'))

qtde = produtos_ecommerce[1][0]
preco = produtos_ecommerce[1][1]
tot = qtde * preco
tot_Plus = qtde * tot
print(f"Tot Vendas SEM Impostos: {tot:.2f}R$")



if 'livro' in produtos:
    # Variavel recebe Index do Item/produto
    i_livro = produtos.index('livro')
    # mostra Equivalencia de posição entre as duas listas:
    print('Quantidade', produtos_ecommerce[i_livro][0], "\nPreço ", produtos_ecommerce[i_livro][1], "R$")
    # É possivel alternar entre itens das sub-listas -> Neste caso 1 é o segundo Item.
    tributo = (produtos_ecommerce[i_livro][1] / 100) * 10 + produtos_ecommerce[i_livro][1]
    print(f"Preço Final Com imposto de 10%: {tributo}R$")

    Novo_Total = (tributo * qtde)
    print("Tot em Vendas de Livros (Com Impostos): {:,}".format(Novo_Total))

    Imposto_Sob_Valor = Novo_Total - tot
    print("Imposto Sob o Valor Total de Vendas de Livros: {:,}: ".format( Imposto_Sob_Valor))



    # Solução do professor:  (Tive que usar a var X pois não estamos no Jupyter_Notebook)
    # x = produtos_ecommerce[i_livro][0] = produtos_ecommerce[i_livro][1] * 1.1
    # print(x)


