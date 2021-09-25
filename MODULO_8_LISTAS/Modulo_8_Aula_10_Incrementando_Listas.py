
lista = ['iphone', 'NoteBook', 'PC']

# Incremento em Listas:
lista = lista + ['Mouse']

print(lista)

lista2 = ['GamePad']

new_List = lista + lista2

print(new_List)

# Incrementando com Numeros (INT):

vendas = 500

soma = vendas + 500

print(soma)

vendas = vendas + soma
print(vendas)

# Me and me myself :
vendas += vendas
print(vendas)


backup = lista.copy()

backup.remove('PC')
print(backup)

mouse = backup.pop()
print(mouse)
