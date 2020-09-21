def main():
    h = 5.50
    c = 6.80
    m = 4.50
    a = 7
    q = 4
    soma = 0

    while True:
        print('CÓDIGO  PRODUTO         PREÇO (R$)')
        print('H       Hamburger       5,50')
        print('C       Cheeseburger    6,80')
        print('M       Misto Quente    4,50')
        print('A       Americano       7,00')
        print('Q       Queijo Prato    4,00')
        print('X       PARA TOTAL DA CONTA')

        codigo = input().upper()[0]

        if codigo == 'X':
            print('{:.2f}'.format(soma))
            break

        if codigo == 'H':
            soma += h
        elif codigo == 'C':
            soma += c
        elif codigo == 'M':
            soma += m
        elif codigo == 'A':
            soma += a
        elif codigo == 'Q':
            soma += q
        else:
            print('Opção inválida.')
        

if __name__ == "__main__":
    main()
