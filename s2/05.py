def main():
    valor = float(input())
    a_vista, cinco_vezes, dez_vezes = valores(valor)
    print('{:.2f}'.format(a_vista))
    print('{:.2f}'.format(cinco_vezes))
    print('{:.2f}'.format(dez_vezes))

def valores(valor):
    a_vista = valor - (valor * 0.09)
    cinco_vezes = valor / 5
    dez_vezes = (valor + (valor * 0.17)) / 10
    return a_vista, cinco_vezes, dez_vezes

if __name__ == '__main__':
    main()