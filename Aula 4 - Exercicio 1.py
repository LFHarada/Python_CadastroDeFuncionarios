import uuid

funcionarios = []

def lista():

    print('\nOlá, seja bem vindo ao sistema de cadastro de funcionários. \n')
    print('Por favor, escolha a opção desejada.\n')

    print('1 - Cadastrar novo funcionário')
    print('2 - Listar funcionários cadastrados')
    print('3 - Procurar funcionário')

    op = int(input('\nOpção: '))

    if op == 1:
        nova = []
        identificador = uuid.uuid4()
        nome = input('Nome completo do funcionário: ')
        nasc = input('Data de nascimento do funcionário: ')
        idade = int(input('Idade atual do funcionário: '))
        cpf = int(input('CPF do funcionário: '))
        for funcionario in funcionarios:
            if funcionario[4] == cpf:
                print('\nEste CPF já está cadastrado. Tente novamente.')
        nova.append(identificador)
        nova.append(nome)
        nova.append(nasc)
        nova.append(idade)
        nova.append(cpf)
        funcionarios.append(nova)

    elif op == 2:
        for funcionario in funcionarios:
            print('\n----------\n')
            print(f'ID: {funcionario[0]};')
            print(f'Nome do funcionário: {funcionario[1]};')
            print(f'Data de nascimento: {funcionario[2]};')
            print(f'Idade: {funcionario[3]};')
            print(f'CPF: {funcionario[4]};')

    elif op == 3:
        cpffuncionario = int(input('CPF do funcionário: '))
        for funcionario in funcionarios:
            if funcionario[4] == cpffuncionario:
                print('----------\n')
                print(f'ID: {funcionario[0]};\n')
                print(f'Nome do funcionário: {funcionario[1]};\n')
                print(f'Data de nascimento: {funcionario[2]};\n')
                print(f'Idade: {funcionario[3]};\n')
                print(f'CPF: {funcionario[4]};\n')
                break
            else:
                print(f'\nFuncionário com CPF {cpffuncionario} não encontrado.')
    else:
        print('Essa opção é inválida.')

while True:
    lista()