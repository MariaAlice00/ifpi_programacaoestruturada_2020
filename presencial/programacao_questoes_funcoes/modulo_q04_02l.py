#2l. Receber um número inteiro de meses e retornar quantos anos e quantos meses ele corresponde.

def anos_meses(meses):
    return meses // 12, meses % 12

def main():
    meses = int(input('Valor em meses: '))
    a, m = anos_meses(meses)
    print(f'{meses} meses equivalem a {a} ano(s) e {m} meses')

if __name__ == '__main__':
    main()