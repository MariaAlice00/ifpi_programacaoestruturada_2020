from random import *

def main():
    executa = True

    adjetivos, hobbies = cumprimentos()

    nome = input('Qual é o seu nome? ')

    print('''
    Menu
    c = obter cumprimento
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobbies
    q = sair
    ''')

    while executa == True:
        menu_choice = input('\n').lower()

        if menu_choice == 'c':
            print('Aqui está o seu cumprimento', nome, ':')
            print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))
            print('De nada!')

        elif menu_choice == 'a':
            item_to_add = input('Adicione o hobby: ')

            if item_to_add not in hobbies:
                hobbies.append(item_to_add)
            else:
                print('O hobby já está na lista!')

        elif menu_choice == 'd':
            item_to_delete = input('Insira o hobby a ser removido: ')

            if item_to_delete in hobbies:
                hobbies.remove(item_to_delete)
            else:
                print('O hobby não está na lista!')

        elif menu_choice == 'p':
            print(hobbies)

        elif menu_choice == 'q':
            executa = False
        else:
            print('Escolha uma opção válida!')


def cumprimentos():
    adjetivos = ['maravilhoso', 'acima da média', 'excelente']
    hobbies = ['andar de bicicleta', 'programar', 'fazer chá']

    return adjetivos, hobbies


if __name__ == "__main__":
    main()