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
    chave_d = 7
    chave_x = 4
    chave_msg = 12

    letra_d = 'd'
    letra_x = 'x'
    msg = 'omqemd'


    alfabeto = letras_alfabeto()

    posicao_d = definir_posicao(alfabeto, letra_d)
    posicao_x = definir_posicao(alfabeto, letra_x)
    posicao_msg = definir_posicao(alfabeto, msg)

    nova_posicao_d = definir_nova_posicao(posicao_d, chave_d)
    nova_posicao_x = definir_nova_posicao(posicao_x, chave_x)
    nova_posicao_msg = definir_nova_posicao(posicao_msg, chave_msg)
    letra_criptografada_d = definir_letra_criptografada(alfabeto, nova_posicao_d)
    letra_criptografada_x = definir_letra_criptografada(alfabeto, nova_posicao_x)
    letra_criptografada_msg = definir_letra_criptografada(alfabeto, nova_posicao_msg)

    print('A letra d criptografada é', letra_criptografada_d)
    print('A letra x criptografada é', letra_criptografada_x)
    print('A mensagem criptografada omqemd é', letra_criptografada_d)


if __name__ == "__main__":
    main()