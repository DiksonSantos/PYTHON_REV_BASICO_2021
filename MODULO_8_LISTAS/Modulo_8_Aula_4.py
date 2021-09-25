produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

# Remove Ultimo elemento:
print(produtos.pop())

# Indice do elemento:
I = produtos.index('mac')
print(I)

produtos.remove(produtos[1])

print(produtos)

# Insere no final da lista:
produtos.append('NoteBook')

# Insere No Indice apontado:
produtos.insert(0, 'Mac_Book_9')

print(produtos, end='\n')

print('\n')

for I in produtos:
    print(I)

# Inserir nome prod input()

try:
    print('\n')
    produtos.remove('Inserir')
except:
    print("Produto Não existe")
    pass
