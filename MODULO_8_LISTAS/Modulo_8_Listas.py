

#
alpha = ['a', 'b', 'c', 'd', 'e']
number = [1, 2, 3, 4, 5]

x = dict(zip(alpha, number))

zipado = x

# print(dict(x))

# Zipado agora é um Dicionario:
print(type(zipado))

"""
for i, j in zipado.items():
    print(f"Chave {i} Valor {j}")
"""
# _______________________________________________________________


# Em qual posição esta um item numa Lista:

I = alpha.index('c')
# print(I)

letra = str(input("Digite a letra: "))

for I in alpha:
    if I == letra:
        print(f"{I} Em Lista: Encontrado")
if I not in letra:
    print('Não Encontrado')

for X in zipado.keys():
    if X == letra:
        print(f"Letra {X} Em Dic Encontrada")
        break
else:
    print('Not Found by now')
