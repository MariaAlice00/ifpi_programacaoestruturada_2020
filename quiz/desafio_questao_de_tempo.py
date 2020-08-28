from time import sleep

def main():
    print('Vou pensar em um número entre 0 e 10.')
    sleep(1)
    print('Eu pensei em qual número?')
    
    numero = input('>>> ')
    
    if numero == '5':
        print('Parabéns!!! Você acertou.')
    else:
        print('Você errou. Que pena.')
    print('Obrigada por jogar!')


if __name__ == "__main__":
    main()
