def main():
    populacao_original = int(input())

    parada = 0.1 * populacao_original
    pop_total = populacao_original
    ano = 1600

    while pop_total > parada:        
        nasc = nascimentos(pop_total)
        morte = mortes(pop_total)
        pop_total = populacao_total(pop_total)

        print('{},{:.0f},{:.0f},{:.0f}'.format(ano, nasc, morte, pop_total))

        ano += 1


def nascimentos(pop_total):
    return 0.01 * pop_total


def mortes(pop_total):
    return 0.06 * pop_total


def populacao_total(pop_total):
    return pop_total - mortes(pop_total) + nascimentos(pop_total)


if __name__ == "__main__":
    main()