# Nothing new until now -_-

tupla__ = ('nome', 'Dikson', 'Santos', 24_03_86)



# Variaveis podem receber pedaços/Indices de tuplas
# nome = tupla[1]
# sobrenome = tupla[2]
# nascimento = tupla[3]

# print(nome, ' ', sobrenome, nascimento)


#DESEMPACOTAMENTO COM EXATA MESMA QUANTIDADE DE ITENS DA TUPLA
x = ident, nome, surname, birt = tupla__

# print(x)

# print(nome)

# print(len(tupla__))


vendas = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Lira', 'Ana', 'Maria', 'Paula']


for i, venda in enumerate(vendas):
    print(f"Funcionario {funcionarios[i]} Vendeu: {venda}")
