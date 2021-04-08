from random import *

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

for attemp in range(3):
    print('\nEscolha uma porta (1, 2 ou 3):')

    porta_escolhida = input()
    porta_escolhida = int(porta_escolhida)

    porta_certa = randint(1, 3)

    print('A porta escolhida foi a', porta_escolhida)
    print('A porta certa é a', porta_certa)

    if porta_escolhida == porta_certa:
        print('Parabéns')
    else:
        print('Que peninha!')