from operator import itemgetter

def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline() 
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
                    "alta": float(alta),
                    "baixa": float(baixa),
                    "fechamento": float(fechamento),
                    "volume": int(volume),
                }
            )
    return linhas


def formatar_data(linha):
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    d, m, a, = linha['dia'], linha['mes'], linha['ano']
    
    return '{:0>2} de {} de {}'.format(d, meses[m - 1], a)


def maior_abertura(linha):
    ordenado = sorted(linha, key=itemgetter('abertura'))

    return ordenado[-1]['abertura'], formatar_data(ordenado[-1])


def main():
    nome_arquivo = input()
    arquivo = carregar(nome_arquivo)

    abert, data = maior_abertura(arquivo)
    print('O maior preço na abertura foi {:.2f} em {}'.format(abert, data))


if __name__ == '__main__':
    main()