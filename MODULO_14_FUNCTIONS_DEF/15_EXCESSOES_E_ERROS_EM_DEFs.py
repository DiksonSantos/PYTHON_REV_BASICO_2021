"""
def descobrir_servidor(email):
    posicao_a = email.index('@')
    servidor = email[posicao_a:]
    if 'gmail' in servidor:
        return 'gmail'
    elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
        return 'hotmail'
    elif 'yahoo' in servidor:
        return 'yahoo'
    elif 'uol' in servidor or 'bol' in servidor:
        return 'uol'
    else:
        return 'não determinado'
"""


def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            print('gmail')
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            # Se o bloco a cima funcionar -> Posso colocar um codigo aqui:
            return 'não determinado'
    except ValueError:
        # print('Sem @')
        # Explode o mesmo erro, poreḿ com a mensagem dentro de ()
        # raise Exception('E-mail Sem @')
        # raise BaseException
        # pass
        return 'Deu erro '

    # Da pra tratar diversos tipo de erros Para qualquer erro que possa aparecer
    except TypeError:
        return 'Erro de Digitação'


email_ = str(input("Email: "))
descobrir_servidor(email_)

# substring not found

"""
Todos os tipos de Except do Python
https://docs.python.org/3/library/exceptions.html
"""
