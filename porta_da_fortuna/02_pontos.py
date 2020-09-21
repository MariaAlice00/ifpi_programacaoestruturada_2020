from random import *

def main():
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

    score = 0

    for attemp in range(3):
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

    print('Pontuação final:', score)


def certa(porta_escolhida, porta_certa):
    return porta_escolhida == porta_certa


if __name__ == "__main__":
    main()