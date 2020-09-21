from random import *

def main():
    jogando = True

    score = 0

    print('''
    Porta da Fortuna!
    =========

    Existe um super prêmio atrás de uma destas 3 portas! Adivinhe qual é a porta certa para ganhar o prêmio!
    _____   _____   _____   
    |     | |     | |     | 
    | [1] | | [2] | | [3] | 
    |   o | |   o | |   o | 
    |_____| |_____| |_____| 
    ''')

    while jogando == True:
        print('\nEscolha uma porta (1, 2 ou 3):')

        porta_escolhida = input()
        porta_escolhida = int(porta_escolhida)

        porta_certa = randint(1, 3)

        print('A porta escolhida foi a', porta_escolhida)
        print('A porta certa é a', porta_certa)

        if certa(porta_certa, porta_escolhida) == True:
            print('Parabéns')
            score += 1
        else:
            print('Que peninha!')
            score = 0

        print('Sua pontuação é:', score)

        print('\nVocê quer jogar de novo? (s/n)')
        resposta = input().lower()

        if parar(resposta) == True:
            jogando = False

    print('Obrigado por jogar.')
    print('Sua pontuação final é de', score)


def certa(porta_escolhida, porta_certa):
    return porta_escolhida == porta_certa


def parar(resposta):
    return resposta == 'n' or resposta == 'nao'


if __name__ == "__main__":
    main()