from random import *

def main():
    print('Gerador de Cumprimentos')
    print('--------------------')

    adjetivos, hobbies, personalidade = cumprimentos()

    nome = input('Qual é o seu nome? ')
    print('Aqui está o seu cumprimento', nome, ':')

    print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))
    print('Além de ser uma pessoa', choice(personalidade))
    print('Parabéns!')


def cumprimentos():
    adjetivos = ['maravilhoso', 'acima da média', 'excelente']
    hobbies = ['andar de bicicleta', 'programar', 'fazer chá', 'cantar', 'cozinhar']
    personalidade = ['divertida', 'alegre', 'de bem com a vida', 'inteligente']

    return adjetivos, hobbies, personalidade


if __name__ == "__main__":
    main()