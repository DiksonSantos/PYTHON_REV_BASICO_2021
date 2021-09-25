lista0 = [1, 2, 3]
lista1 = [4, 5, 6]
lista2 = []
lista3 = []

# GERA CONTINUIDADE NA LISTA (USANDO OUTRA LISTA):
# lista2 = lista0 # Funciona também
lista2.extend(lista0)
lista2.extend(lista1)

print(f"Extensão da L0 coma L1: {lista2}")



lista3.append(lista0)
lista3.append(lista1)

print(f'Lista 3 == append das L0 & L1: {lista3}')

"""
# PERCORRENDO SUB-LISTAS:
for I in lista3:
    for J in I:
        print(J, end='-')
"""


# SOMANDO Numeros selecionados:

juntar = lista0[1] + lista1[2]
print(f'Indices: , L0 Ind:1=-> {lista0[1]}, L1 Ind:2= -> {lista1[2]}')
print('Soma dos Indices: ', juntar)

print(f"Soma de Duas Listas: {lista0 + lista1}")

bagunca = [9,4,7,6,7,8,3,8,5,1,0]

# Decida de do > pro < ou vice versa  com True & False:
bagunca.sort(reverse=True)
print('Sort de uma lista bagunçada: ', bagunca)

bagunca.reverse()
print('Ordem Inversa: ', bagunca)

bagunca.remove(7)
bagunca.remove(8)
bagunca.remove(9)
bagunca.insert(2, 2)# 2 na posição Dois (Indice , elemento)
bagunca.insert(10, 9)# Insere 9 na posição 10 
print(bagunca)
