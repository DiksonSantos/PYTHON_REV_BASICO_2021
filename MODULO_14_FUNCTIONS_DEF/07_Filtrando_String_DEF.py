emails = ['diksonnn@gmail.com', 'dikson_santos@outlook.com',
          'gowdikson@hotmail.com', 'dikson.enterprise@gmail.com']


def filtra(lista, texto):
    filtrada = []
    for item in lista:
        if texto in item:
            filtrada.append(item)
    return filtrada


print(f"Gmails: {filtra(emails, 'gmail')}")

print(f"Hotmails: {filtra(emails, 'hotmail.com')}")
