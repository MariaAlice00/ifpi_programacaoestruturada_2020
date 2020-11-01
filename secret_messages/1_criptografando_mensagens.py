def letras_alfabeto():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    return alfabeto


def definir_posicao(alfabeto, letra):
    posicao = alfabeto.find(letra)

    return posicao


def definir_nova_posicao(posicao, chave):
    nova_posicao = (posicao + chave) % 26 # retornar para 0 quando chegar no 26
    
    return nova_posicao


def definir_letra_criptografada(alfabeto, nova_posicao):
    letra_criptografada = alfabeto[nova_posicao]

    return letra_criptografada


def main():
    chave = 3

    letra = input('Por favor, entre com uma letra para criptografar: ')

    alfabeto = letras_alfabeto()
    posicao = definir_posicao(alfabeto, letra)
    nova_posicao = definir_nova_posicao(posicao, chave)
    letra_criptografada = definir_letra_criptografada(alfabeto, nova_posicao)

    print('Sua letra criptografada é', letra_criptografada)


if __name__ == "__main__":
    main()