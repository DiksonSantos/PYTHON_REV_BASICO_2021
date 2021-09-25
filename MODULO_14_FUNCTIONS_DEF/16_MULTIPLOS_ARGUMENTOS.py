def minha_soma(*numeros):
    print(numeros)
    # Variavel auxiliar
    soma = 0
    # Percorre os elementos da tupla
    for numero in numeros:
        # Soma os elementos da tupla
        soma += numero
    return soma

"""
def preco_final(preco, **adicionais):
    ''' *** gera um Dicionario com CHave / Valor'''
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco
"""

# print('Tipos de Argumentos:\n'   'desconto, garantia_extra, imposto')
"""
# Função não funciona com inputs, De jeito nenhum 
preco_ = int(input('Preço: '))
desconto_ = float(input('Desconto ? '))
gar = int(input('Garantia? '))
imposto = float(input('Impostos? '))
"""


# print(preco_final(1000, desconto=0.1, garantia_extra=100, imposto=0.3))
# print(preco_final(preco_, desconto_, gar, imposto))


def cumprimento_especia(**kwargs):
    if 'Gow' in kwargs and kwargs['Gow'] == 'Python':  # -> Se Gow estiver no Dicionario & o Valor de Gow for Python:
        return 'Você é Féra Mesmo!'
    elif 'Gow' in kwargs:  # Se Gow Estiver no Dicionario porém Valor informado NÃO é Python:
        return f'{kwargs["Gow"]} Valor Não é Python'
    return 'A Chave Informada NÃO É GOW'  # <- Se a Chave Informada á Função NÃO for Gow


'''No caso aqui corresponde ao primeiro IF'''
guardar = cumprimento_especia(Gow='Python')  # Chave = Gow & Valor = Python
# print(guardar)  # Retorna -> Voce é fera mesmo

guardar1 = cumprimento_especia(Nope='Python')
# print(guardar1)

'''Se Gow for a chave -> Retorne o valor *Gow_Dikson* logo após o valor informado
depois de *Gow*'''
guardar3 = cumprimento_especia(Gow='Nome')
# print(guardar3)  # Mostrou na ordem inversa O valor Depois a Chave da linha de cima.

guardar4 = cumprimento_especia(Gw='Pyt')
# print(guardar4)

VAZIO = cumprimento_especia()
# print(VAZIO)  # -> A Chave Informada NÃO É GOW


# SOLUÇÃO DO FORUM DE RESPOSTAS:

def preco_final(preco, **adicionais):

    ''' *** gera um Dicionario com CHave / Valor'''

    print(adicionais)

    if 'desconto' in adicionais:

        preco *= (1 - adicionais['desconto'])

    if 'garantia_extra' in adicionais:

        preco += adicionais['garantia_extra']

    if 'imposto' in adicionais:

        preco *= (1 + adicionais['imposto'])

    return preco



# print('Tipos de Argumentos:\n'   'desconto, garantia_extra, imposto')


# Função não funciona com inputs, De jeito nenhum

preco_ = int(input('Preço: '))

desconto_ = float(input('Desconto ? '))

gar = int(input('Garantia? '))

imposto = float(input('Impostos? '))




# print(preco_final(1000, desconto=0.1, garantia_extra=100, imposto=0.3))

# SOLUÇÃO DO FORUM:
# Inventaram nomes/variaveis para receberem as outras 3 entradas necessárias.
print(preco_final(preco_, d=desconto_, g=gar, i=imposto))
