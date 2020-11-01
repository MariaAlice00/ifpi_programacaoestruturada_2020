def letras_alfabeto():
    alfabeto =  'qwertyuiopasdfghjklzxcvbnm'

    return alfabeto


def criptografar(mensagem):
    alfabeto = letras_alfabeto()

    mensagem_criptografada = ''
    chave = 1

    for letra in mensagem:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)

            nova_posicao = (posicao + chave) % 26

            mensagem_criptografada += alfabeto[nova_posicao]

            chave += 1            
        
    mensagem_criptografada = mensagem_criptografada.split()
    mensagem_criptografada = ''.join(mensagem_criptografada)

    return mensagem_criptografada


def main():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    mensagem = input('Por favor, entre com a mensagem a ser criptografada: ').lower()

    mensagem_criptografada = criptografar(mensagem)

    print('Sua mensagem criptografada é:', mensagem_criptografada)


if __name__ == "__main__":
    main()