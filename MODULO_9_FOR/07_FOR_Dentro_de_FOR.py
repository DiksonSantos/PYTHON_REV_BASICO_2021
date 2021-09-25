
estoque = [
    [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
    [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
    [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
    [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
    [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
]
fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
nivel_minimo = 50

consta = []
# Percorre a quantidade de Listas dentro da Lista 'estoque' :
for I, lista in enumerate(estoque):
    # Percorrendo os itens dentro das sub-listas
    for J in lista:
        # Se um desses itens (da lista estoque) for menor que o 1nivel minimo'
        if J < nivel_minimo:
            # mostre seus equivalentes (em posição) da outra lista
            # Caso haja algum item em Sub-Listas que seja menor que 50, esta fábrica sera mostrada
            # print(fabricas[I])
            if fabricas[I] not in consta:
                # pass
            # else:
                consta.append(fabricas[I])
            print(f"Item em baixa: {J} Fábrica: {fabricas[I]}")

print(f"Constam itens a Baixo do Minimo em :: {consta}")

'''
for k in consta:
    print(k, end='\n')
'''
