produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']


print('Usando o JOIN como separador de intens:')
# print(' - '.join(produtos), '\n')

"""
print('Usando end= Como separador:')
for I in produtos:
    print(I, end=' - ')
"""


lista_prod = 'apple tv, mac, iphone x, IPad, apple watch, mac book, airpods'

'''Transforma Uma STRING numa LISTA e Separa os Itens da Lists com
(neste caso) Virgulas (",") '''
print('Split de Strings: ')
print(lista_prod.split(','))

# Convertendo String Para Lista Com separadores pré determinados:
# Retira o espaço entre a primeira ' e o item -> Use um espaço depois da virgula.
conv = list(lista_prod.split(', '))

print("\nConvertendo String Para Lista com Separadores Pré Determinados:")
print(conv)
