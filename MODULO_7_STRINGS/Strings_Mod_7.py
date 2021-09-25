"""
nome = str(input('Nome: ')).rstrip().lstrip().capitalize()
surname = str(input('Sobrenome: ')).rstrip().lstrip().capitalize()

print(f'Qtd_Letras {len(nome) + len(surname)}, \n Nome: {nome} ', surname)
"""


"""
print("Digite Apenas Numeros Sem Pontos ou '-'")
cpf = input('Isira o CPF: ').strip().rstrip().replace('.', '').replace('-', '').replace(',', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite Apenas os Numeros do Seu CPF')
"""


"""
# LOGIN

name = input('Nome: ')
email = input('Email: ')

if name and email:
    pos_a = email.find('@')
    # Caso ele não encontre ,no caso o @ ou o que quer que esteja em .find(), ele sempre retorna -1

    # Do @ até o final
    servidor = email[pos_a:]

    # OU -> Caso encontr o @ em uma das Duas Variaveis (Nome & Email)
    # Caso tenha ponto final do @ até o final (ou) depois do @ (ALL OK):
    if pos_a != -1 and '.' in servidor:
        # Imprima a mensagem:
        print('Cadastro Concluido')
    else:
        print("Email Invalido")
else:
    print('Digite email corretamente')


"""
custo = 5000
faturamento = 2700
lucro = faturamento - custo
# print('Faturamento foi {:+,} e lucro foi {:+}'.format(faturamento, lucro))
# Usando Fstring:
print(f'Faturamento foi {faturamento:+,} e lucro foi {lucro:+,}')

print(f'Faturamento foi {faturamento:.2f} e lucro foi {lucro:.2f}')




