dic = {}

dic['chave'] = 'valor'

print(dic)


# APPEND EM DICIONARIO:
dic.update({'key': 'value'})


print(dic)
# {'chave': 'valor', 'key': 'value'}


# SE ADD UMA CHAVE DE NOME JÁ EXISTENTE -> ELE SUBSTITUI O VALOR DESTA:
dic['chave'] = 'VALOR__'

print(dic)
# {'chave': 'VALOR__', 'key': 'value'}

# REMOVENDO:
del dic['key']

print(dic)

chave = dic.pop('chave')
print(dic)

# ARMAZENA O VALOR DA CHAVE REMOVIDA COM POP:
print(chave)

dic['Dikson'] = 'Santos'
print(dic)

# LIMPA UM DICIONARIO:
dic.clear()
print(dic)
# {}


# DELETA DICIONARIO COM TUDO:
del dic
# print(dic)
# 'dic' is not defined


dic = {}
dic["Dikson"] = 35
print(dic)
