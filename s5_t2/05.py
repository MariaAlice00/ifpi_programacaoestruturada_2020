def main():
    valor_compra = float(input())

    for c in range(1, 25):
        valor_prestacao = valor_compra / c
        print('{}x de R$ {:.2f}'.format(c, valor_prestacao))


if __name__ == "__main__":
    main()
