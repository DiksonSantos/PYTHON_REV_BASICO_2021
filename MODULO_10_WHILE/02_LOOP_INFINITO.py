vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50


# While é parecido com o FOR no que diz respeito a Percorrer Listas:

i = 0

# Issogera um Loop nfinito, pois -> Todas as vendas são maiores que méta:
while vendas[i] > meta:
    i += 1 # Adicionando esta Linha -> Deixa de ser Infinito
    print(f"{vendedores[i]} Bateu a meta com {vendas[i]} Vendas")
