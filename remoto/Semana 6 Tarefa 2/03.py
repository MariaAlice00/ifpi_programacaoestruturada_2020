def main():
    while True:
        print('OPÇÕES:')
        print('1 - SAUDAÇÃO')
        print('2 - BRONCA')
        print('3 - FELICITAÇÃO')
        print('0 - FIM')
        opcao = int(input())

        if opcao == 1:
            print(f'{1} - Olá. Como vai?')
        elif opcao == 2:
            print(f'{2} - Vamos estudar mais.')
        elif opcao == 3:
            print(f'{3} - Meus Parabéns!')
        elif opcao == 0:
            print(f'{0} - Fim de serviço.')
            break
        else:
            print('Opção inválida.')


if __name__ == "__main__":
    main()