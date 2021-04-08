# Qual o preço médio de abertura em um mês e ano informados?

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


def abertura_media(arquivo, mes, ano):
    soma = 0
    q = 0
    for dado in arquivo:
        if dado['mes'] == mes and dado['ano'] == ano:
            soma += dado['abertura']
            q += 1

    media = soma / q

    return media


def main():
    nome_arquivo = input()
    nome_arquivo = nome_arquivo.replace('\r','')
    arquivo = carregar(nome_arquivo)

    mes = int(input())
    ano = int(input())

    media = abertura_media(arquivo, mes, ano)

    print('O preço médio de abertura em {}/{} foi {:.2f}'.format(mes, ano, media))


if __name__ == '__main__':
    main()