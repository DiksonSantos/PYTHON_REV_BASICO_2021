"""
SET  -> Usa colchetes, mas Não é Dicionario
Ordem aleatoria -> Não é possivel buscar por indice/posição
Sempre embralha a ordem dos itens

"""


set_produtos = {'arroz', 'feijao', 'macarrao', 'atum', 'azeite'}

print(set_produtos)

# Converter uma lista para um SET para saber se existem valores repetidos nela
cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

set_cpfs = set(cpf_clientes)
print('Tamanho do CPF_Clientes: ', len(cpf_clientes))
print('Tamanho do SET: ', len(set_cpfs))
# Tinham 3 repetidos


# Nova Lista (SEM Clientes Repetidos):
CPFs_Unicos = set_cpfs
print(f'Lista Sem repetições: {len(CPFs_Unicos)}', CPFs_Unicos)
