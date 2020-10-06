def main():
    populacao = int(input())

    informacoes = carrega_cidades()

    print('CIDADES COM MAIS DE {} HABITANTES:'.format(populacao))
    for dado in informacoes:
        if dado[5] > populacao:
            ibge = dado[1]
            nome = dado[2]
            uf = dado[0]
            print('IBGE: {} - {}({}) - POPULAÇÃO: {}'.format(ibge, nome, uf, dado[5]))


def carrega_cidades():
    informacoes = []
    
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            informacoes.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()

    informacoes = tuple(informacoes)
    return informacoes


if __name__ == "__main__":
    main()
