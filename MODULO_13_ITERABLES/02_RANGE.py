funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro',
                'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

print("Funcionarios Classe B")
for i in range(2, 18, 1):
    print(f"Funcionarios: {funcionarios[i]}, Vendas: {vendas[i]}")

convidados = ['Maria', 'José', 'Antônio', ]
# Convidados:
for i in range(len(convidados)):
    if funcionarios[i] in convidados[i]:
        print(f'Esta na lista: {convidados[i]} ')
