def main():
    deposito_inicial = float(input())
    taxa_juros = float(input())
    
    a = anos(deposito_inicial, taxa_juros)
    print(a)


def anos(deposito_inicial, taxa_juros):
    anos = 1
    valor = deposito_inicial

    while True:
        juros = (taxa_juros / 100) * valor
        valor += juros

        if valor > 2 * deposito_inicial:
            break
        
        anos += 1

    return anos


if __name__ == "__main__":
    main()
