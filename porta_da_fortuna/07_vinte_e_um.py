from random import *

def main():
    print('''
    Vinte e um !
    ============
    Tente fazer exatamente 21 pontos!
    ''')

    jogando = True
    pontuacao = 0

    while jogando == True:
        num = randint(1, 10)
        pontuacao += num

        print('Número:', num)
        print('Sua pontuação agora é:', pontuacao)

        print('Gostaria de somar mais um número? (s/n)')
        resposta = input()
        if resposta == 'n':
            jogando = False

    print('Sua pontuação final é', pontuacao)
    
    if pontuacao == 21:
        print('Parabéns!!!')
    else:
        print('Não foi dessa vez.')

    print('Obrigada por jogar!')


if __name__ == "__main__":
    main()
