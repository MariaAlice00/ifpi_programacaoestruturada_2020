from operator import itemgetter

def carregar(arquivo):
    dados = []
    with open(arquivo) as f:
        f.readline() 
        for candidato in f.readlines():
            nome, numero, partido, coligacao, total_votos_validos = candidato.strip().split(';')
            dados.append(
                {
                    "nome": str(nome),
                    "numero": int(numero),
                    "partido": str(partido),
                    "coligacao": str(coligacao),
                    "total_votos_validos": int(total_votos_validos)
                }
            )

    return dados


def organizar(candidato):
    dados_organizados = sorted(candidato, key=itemgetter('total_votos_validos'), reverse=True)

    return dados_organizados


def imprimir(candidato):
    dados_organizados = organizar(candidato)
    print('DADOS DOS CANDIDATOS')
    print('Número  Nome do Candidato                  Votos * Partido (coligação)')
    for candidato in dados_organizados:
        print('{}   '.format(candidato['numero']), end='')
        print('{}'.format(candidato['nome']), end='')
        print(' ' * (36 - len(candidato['nome'])), end='')
        print('{} * {} ({})'.format(candidato['total_votos_validos'], candidato['partido'], candidato['coligacao']))


def main():
    nome_arquivo = input()
    arquivo = carregar(nome_arquivo)
    
    imprimir(arquivo)


if __name__ == '__main__':
    main()
