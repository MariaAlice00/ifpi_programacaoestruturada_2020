#2e. Receber uma quantidade de anos e meses retornar o número inteiro de meses que ele corresponde.

def main():
    a = int(input('Quantidade de anos: '))
    m = int(input('Quantidade de meses: '))
    meses(a, m)
    print(f'{a} anos e {m} meses equivalem a {meses(a, m)} meses')

def meses(a, m):
    return (a * 12) + m

if __name__ == '__main__':
    main()