vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000


# PARA USAR 'IF' EM LIST_COMPREHENSION -> USE OS IFs ANTES DOS FORs

# variavel = [item if condição else outro_resultado for item in iterable]



# COMO SE FAZ COM DICIONARIOS:
bonus = [(vendedores_dic[V] / 100)*10 if vendedores_dic[V] > meta else 'não' for V in vendedores_dic]
print(bonus)
