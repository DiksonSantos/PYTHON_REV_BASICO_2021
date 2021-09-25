from collections import Counter

produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]

top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

tot_tot = 0
tot_5 = 0
for I, J in enumerate(vendas):
    tot_tot += J
    if produtos[I] in top5:
        tot_5 += J
        print(produtos[I], J)
print('Soma dos Top 5 Mais Vendidos: ', tot_5)
print('Total Absoluto Vendido: ', tot_tot)
top_vendas = tot_5 / tot_tot * 100
print(f'Os 5 Mais representam {top_vendas:.1f}% das Vendas totais')


# SOLUÇÃO EM LIST COMPREHENSION:
total_top_5 = sum(vendas[i] for i, produto in enumerate(produtos) if produto in top5)
print(total_top_5)
