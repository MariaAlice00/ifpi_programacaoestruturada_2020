def main():
    lista = []

    while True:
        print('1 - Incluir Novo Nome')
        print('2 - Incluir Telefone')
        print('3 - Excluir Telefone')
        print('4 - Excluir Nome')
        print('5 - Mostrar Agenda')
        print('0 - Fim do programa')

        opcao = int(input('>>> '))

        if opcao == 1:
            incluir_nome(lista)

        elif opcao == 2:
            incluir_telefone(lista)

        elif opcao == 5:
            mostrar_agenda(lista)

        elif opcao == 0:
            print('Saindo do programa...')
            break

        else:
            print('Opção inválida. Por favor, tente novamente')


def incluir_nome(lista):
    nome = input('Nome: ')
    telefones = []

    telefone = input('Telefone: ')
    telefones.append(telefone)

    cont = input('Deseja adicionar mais um telefone? [S/N]: ').upper()
    while True:
        if cont == 'N':
            break
        elif cont == 'S':        
            telefone_novo = input('Telefone: ')
            telefones.append(telefone_novo)

        cont = input('Deseja adicionar mais um telefone? [S/N]: ').upper()

    contato = {
        'nome': nome,
        'telefone': telefones
    }

    lista.append(contato)

    print('O contato foi cadastrado com sucesso!')

    return lista, telefones


def incluir_telefone(lista):
    lista, telefones = incluir_nome(lista)
    while True:
        nome = input('Digite o nome do contato que você quer adicionar o telefone:  ')

        if existe_contato(lista, nome):
            telefone = input('Digite o telefone: ')
            telefones.append(telefone)
            break
        else:
            c = input('Esse nome não existe.\n Deseja incluí-lo? [S/N]: ').upper()
        
            if c == 'S':
                incluir_nome(lista)
            elif c == 'N':
                print('Tudo bem.')
    
    print('Cadastrado!')


def existe_contato(lista, nome):
    if len(lista) > 0:
        for contato in lista:
            if contato['nome'] == nome:
                return True
        
    return False



def mostrar_agenda(lista):
    print('=========== LISTAR CONTATOS ==============')
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print('Contato {}:'.format(i+1))
            print('\tNome: {}'.format(contato['nome']))
            print('\tTelefone(s): {}'.format(contato['telefone']))
            print('====================================')
        print('Quantidade de contatos: {}\n'.format(len(lista)))
    else:
        print('Não existem nenhum contato cadastrado no sistema.\n')


if __name__ == "__main__":
    main()
