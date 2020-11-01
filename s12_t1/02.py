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


def menor_fechamento(linha):
    ordenado = sorted(linha, key=itemgetter('fechamento'))

    return ordenado[0]['fechamento'], formatar_data(ordenado[0])


def main():
    nome_arquivo = input()
    nome_arquivo = nome_arquivo.replace('\r','')
    arquivo = carregar(nome_arquivo)

    fecham, data = menor_fechamento(arquivo)
    print('O menor preço no fechamento foi {:.2f} em {}'.format(fecham, data))


if __name__ == '__main__':
    main()