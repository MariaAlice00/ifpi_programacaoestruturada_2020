def main():
    mes = int(input())
    populacao = int(input())

    informacoes = carrega_cidades()

    m = mes_extenso(mes)
    print('CIDADES COM MAIS DE {} HABITANTES E ANIVERSÁRIO EM {}:'.format(populacao, m))
    for dado in informacoes:
        if dado[5] > populacao and dado[4] == mes:
            nome = dado[2]
            uf = dado[0]
            dia = dado[3]
            print('{}({}) tem {} habitantes e faz aniversário em {} de {}.'.format(nome, uf, dado[5], dia, m.lower()))


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


def mes_extenso(mes):
    if mes == 1:
        return 'JANEIRO'
    if mes == 2:
        return 'FEVEREIRO'
    if mes == 3:
        return 'MARÇO'
    if mes == 4:
        return 'ABRIL'
    if mes == 5:
        return 'MAIO'
    if mes == 6:
        return 'JUNHO'
    if mes == 7:
        return 'JULHO'
    if mes == 8:
        return 'AGOSTO'
    if mes == 9:
        return 'SETEMBRO'
    if mes == 10:
        return 'OUTUBRO'
    if mes == 11:
        return 'NOVEMBRO'
    if mes == 12:
        return 'DEZEMBRO'


if __name__ == "__main__":
    main()