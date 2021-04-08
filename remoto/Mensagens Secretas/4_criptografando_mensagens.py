def letras_alfabeto():
    alfabeto =  'abcdefghijklmnopqrstuvwxyz'

    return alfabeto


def criptografar(mensagem, chave):
    alfabeto = letras_alfabeto()

    mensagem_criptografada = ''

    for char in mensagem:
        if char in alfabeto:
            posicao = alfabeto.find(char)

            nova_posicao = (posicao + chave) % 26

            mensagem_criptografada += alfabeto[nova_posicao]
        
        else:
            mensagem_criptografada += char

    return mensagem_criptografada


def main():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    mensagem = input('Por favor, entre com a mensagem a ser criptografada: ').lower()

    chave = int(input('Por favor, entre a chave: '))

    mensagem_criptografada = criptografar(mensagem, chave)

    print('Sua mensagem criptografada é:', mensagem_criptografada)


if __name__ == "__main__":
    main()