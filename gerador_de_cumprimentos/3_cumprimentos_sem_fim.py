from random import *

def main():
    executa = True

    adjetivos, hobbies = cumprimentos()

    nome = input('Qual é o seu nome? ')

    print('''
    Menu
    c = obter cumprimento
    q = sair
    ''')

    while executa == True:
        menu_choice = input('\n').lower()

        if menu_choice == 'c':
            print('Aqui está o seu cumprimento', nome, ':')
            print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))
            print('De nada!')
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