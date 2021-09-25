vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000
print(f"Meta De vendas = {meta}")
res = ''
atingiram_meta = 0
Natingiram_meta = 0
for Item in vendas:
    if Item > meta:
        res = 'Meta Atingida'
        atingiram_meta += 1
        print(Item, res,)
    else:
        res = 'NÃO Atingida'
        Natingiram_meta += 1
        print(Item, res)

    # print(res)
print("Quantidade de Itens Analisados: ", len(vendas))
print(f"{atingiram_meta} -> Atingiram Meta de Vendas")
print(f"{Natingiram_meta} -> Não Atingiram Meta")
percentual = atingiram_meta / len(vendas)
print(f"Percentual de Pessoas que bateram a meta De Vendas:{percentual:.1%}")
