codigos = ['nan ', 'mAn  ', '  MAIo', '  SeT   ']


def standar_text(lista_cod, stand='m'):
    for i, item in enumerate(lista_cod):
        item = item.replace('  ', ' ')
        item = item.strip()
        if stand == 'm':
            # CaseFold == Tudo do mesmo tamanho...
            item = item.casefold()
        elif stand == 'M':
            item = item.upper()
        # Neste caso [i] funciona por causa do uso do Enumerate
        lista_cod[i] = item
    return lista_cod


# Tudo Minusculo:
print(standar_text(codigos, 'm'))

# Tudo Maiusculo:
print(standar_text(codigos, 'M'))

# Valor padrão definido com default na DEF == Tudo Minusculo
print(standar_text(codigos))
