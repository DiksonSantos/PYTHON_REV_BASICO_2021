"""
Exercícios
1. Criando um Registro de Hóspedes

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel,
 os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

    1 - Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto
     (perguntando por meio de input)
    2 - De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf
     e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa,
      UM para o cpf e outro para o nome)
    3- O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em
    que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

"""

# Qtd Pessoas
# for range(qtd_pessoas)
# dentro do for -> input de CPFs & Input para nome desta qtd de pessoas
# .append numa lista contendo Nome & CPF de cada pessoa
'''
string = ''
quarto = []
qtd_person = int(input('Informe a qantidade de Pessoas: '))
for I in range(qtd_person):
    nome = str(input("Informe Nome: "))
    cpf = int(input('Informe o CPF:'))
    string = nome, cpf
    quarto.append(string)
"""
#Solução da Renata (Aluna prodigia)
for i in quarto:
    indice = quarto.index(i)
    print(f"Nome: {quarto[indice][0].capitalize()}, CPF: {quarto[indice][1]}")
"""
# Minha solução (simples) :0
for I in quarto:
    print(f"Nome: {quarto[0][0].capitalize()}, \nCPF: {quarto[0][1]}")
'''
# __________________________________________________________________________________________

# EXERCICIO 02 -> ANALISE DE VENDAS:

"""
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

#print(vendas[1][1])

for I, J in vendas:
    if J > meta:
        print(f"Vendedor {I},Vendeu: {J} Bateu Meta !")
"""

# EXERCICIO 03. Comparação com Ano Anterior
'''
Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

Dica: lembre do enumerate, ele pode facilitar seu "for"
'''

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell',
            'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467,
              489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633,
              725316, 644622, 994303]

# vendas2020 = [1,2,3]
# vendas2019 = [4,5,6]

# produtos tiveram no ano de 2020 mais vendas do que no ano de 2019
# o % de crescimento de 2020 para 2019
# para calcular o % de crescimento de um produto de um ano para o outro -> (vendas_produto2020/vendas_produto2019 - 1)

# RELACIONAR UMA LISTA DE STRINGs E UMA NUMERICA:
for I, produto in enumerate(produtos):
    # Se Vendas de 2020[Prod Relacionado em Produtos] Maior que 2019:
    # O FOR e ENUMERATE esta percorrendo a lista de Strings Assim [I] vai procurar um equivalente em posição em qualquer outra lista citada no laço FOR
    if vendas2020[I] > vendas2019[I]:
        # Esta variavel o recebe & o divide por seu equivalente de 2019 (Já o -1 é um mistério ainda)
        crescimento_vendas = vendas2020[I] / vendas2019[I] - 1
        print(F"Produto {produto.upper()} Vendeu {vendas2019[I]} em 2019 & {vendas2020[I]} Unidades Em 2020. \n"
              F"Crescimento de: {crescimento_vendas:.1%}")
