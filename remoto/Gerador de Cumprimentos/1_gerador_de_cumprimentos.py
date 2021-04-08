from random import *

def main():
    print('Gerador de Cumprimentos')
    print('--------------------')

    adjetivos, hobbies = adjetivos_hobbies()

    nome = input('Qual é o seu nome? ')
    print('Aqui está o seu cumprimento', nome, ':')

    print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))
    print('De nada!')


def adjetivos_hobbies():
    adjetivos = ['maravilhoso', 'acima da média', 'excelente']
    hobbies = ['andar de bicicleta', 'programar', 'fazer chá']

    return adjetivos, hobbies


if __name__ == "__main__":
    main()