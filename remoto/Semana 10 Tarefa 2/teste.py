def existe_contato(lista, email):
    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True
        
    return False


def adicionar(lista):
    while True:
        email = input('Digite o e-mail do contato: ')

        if not existe_contato(lista, email):
            break
        else:
            print('Esse e-mail já foi utilizado.\n Por favor, tente um novo e-mail.')

    contato = {
        'email': email,
        'nome': input('Digite o nome: '),
        'telefone': input('Digite o telefone: ')
    }

    lista.append(contato)

    print('O contato {} foi cadastrado com sucesso!\n'.format(contato['nome']))



def alterar():
    pass

def excluir():
    pass

def buscar():
    pass

def listar(lista):
    print('=========== LISTAR CONTATOS ==============')
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print('Contato {}:'.format(i+1))
            print('\tNome: {}'.format(contato['nome']))
            print('\tEmail: {}'.format(contato['email']))
            print('\tTelefone: {}'.format(contato['telefone']))
            print('====================================')
        print('Quantidade de contatos: {}\n'.format(len(lista)))
    else:
        print('Não existem nenhum contato cadastrado no sistema.\n')


def principal():
    lista = []

    while True:
        print('=== Agenda Telefônica ===')
        print('1 - Adicionar contato')
        print('2 - Alterar contato')
        print('3 - Excluir contato')
        print('4 - Buscar contato')
        print('5 - Listar contatos')
        print('0 - Sair')

        opcao = int(input('>>> '))

        if opcao == 1:
            adicionar(lista)
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar(lista)
        elif opcao == 0:
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Por favor, tente novamente')


principal()