"""
def calcula_preco(preco):
    return preco * 0.1
"""

def calcula_imposto(imposto):
    '''Imposto será aplicado numa função Lambda
     que recebe o parametro "Preco" '''
    return lambda preco: preco * (1 + imposto)



# Aqui a variavel calc_prec... Representa a Lambda de dentro da função
# ..ela esta recebendo e multiplicando uma função (DEF) , representada por 'calcula_imposto'
calc_prec_prod = calcula_imposto(0.1)
calc_prec_serv = calcula_imposto(0.15)
calc_preco_royalties = calcula_imposto(0.25)

# print(int(calc_prec_prod(100)))

print(f'{calc_prec_prod(100):.1f}%')
print(int(calc_prec_serv(100)))
print(f'{calc_preco_royalties(100):.1f}%')


# produto 0.1
#serviço 0.15
#royalties 0.25
