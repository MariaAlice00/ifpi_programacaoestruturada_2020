def main():
    carro = float(input())
    meses = mes(carro)
    print(meses)


def mes(carro):
    dinheiro = 10000
    mes = 0

    while dinheiro <= carro:
        taxa_carro = (0.4 / 100) * carro
        taxa_dinheiro = (0.7 / 100) * dinheiro

        carro += taxa_carro
        dinheiro += taxa_dinheiro
        mes += 1

    return mes


if __name__ == "__main__":
    main()