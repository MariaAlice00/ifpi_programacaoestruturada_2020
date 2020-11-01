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


def variacao(arquivo, mes, ano):
    escolhidos = []
    dicionario = {}

    for dado in arquivo:
        if dado['mes'] == mes and dado['ano'] == ano:
            if dado['abertura'] > dado['fechamento']:
                data = '{:0>2}/{:0>2}/{}'.format(dado['dia'], dado['mes'], dado['ano'])

                variacao = dado['abertura'] - dado['fechamento']
                variacao = round(variacao, 2)

                dicionario['data'] = data
                dicionario['abertura'] = dado['abertura']
                dicionario['fechamento'] = dado['fechamento']
                dicionario['variacao'] = variacao

                escolhidos.append(dicionario.copy())

    escolhidos = sorted(escolhidos, key=itemgetter('data'))

    return escolhidos


def main():
    nome_arquivo = input()
    nome_arquivo = nome_arquivo.replace('\r','')
    
    arquivo = carregar(nome_arquivo)

    mes = int(input())
    ano = int(input())

    print('Dias de {}/{} que houve queda no preço da ação:'.format(mes, ano))
    
    escolhidos = variacao(arquivo, mes, ano)
    for linha in escolhidos:
        print('(\'{}\', {}, {}, {})'.format(linha['data'], linha['abertura'], linha['fechamento'], linha['variacao']))
        

if __name__ == '__main__':
    main()
