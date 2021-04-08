'''Suponha que vamos jogar um dado e queremos saber quantas vezes cada face (de 1 a 6) caiu. Faça um programa que leia o resultado de cada jogada do dado e armazena em um dicionário. A face do dado é a chave para o dicionário e a leitura de um valor 0 (zero) na face encerra o jogo. Mostre quantas vezes o dado foi lançado e quantas vezes cada face saiu.'''

def formar_lista_de_jogadas():
    jogadas = []
    vezes = 0

    while True:
        ano = int(input())

        if ano == 0:
            break
        
        jogadas.append(ano)

        vezes += 1

    jogadas.sort()

    return vezes, jogadas


def separando(jogadas):
    dicionario = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for c in jogadas:
        if c not in dicionario:
            dicionario[c] = 1
        else:
            dicionario[c] += 1

    return dicionario


def main():
    vezes, jogadas = formar_lista_de_jogadas()

    print('O dado foi lançado {} vezes.'.format(vezes))

    dicionario = separando(jogadas)
    for k, v in dicionario.items():
        print('A face {} saiu {} vezes.'.format(k, v))


if __name__ == "__main__":
    main()