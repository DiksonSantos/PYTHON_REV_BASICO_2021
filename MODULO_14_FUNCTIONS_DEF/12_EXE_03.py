meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}


def reach_goal(vendors, goal):
    tot_vendors = 0
    med = 0
    atingiram = []
    for I, J in vendors.items():
        if J >= goal:
            tot_vendors += 1
            atingiram.append(I)
    med = (tot_vendors / len(vendors)) * 100

    print(f'Vendedo(res) {atingiram} Atingiram a Meta de vendas.'
          f'\n Total de Vendedores que atingiram meta: {med}%')


reach_goal(vendas, meta)

"""
def reach_meta(vendedor, meta):
    for vendor, venda_ in vendedor:
        if vendor[1] > meta:
            print(f'O vendedor {vendedor} vendeu {venda_} atingindo a meta {meta}')
    return 'OK'


reach_meta(vendedor=vendas, meta=meta)
"""
