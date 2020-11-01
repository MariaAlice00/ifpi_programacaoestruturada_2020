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

    mensagem_1 = 'Oi, tudo bem?'
    mensagem_2 = 'Como vai?'
    mensagem_3 = 'Eu sou demais!'

    chave = 5

    mensagem_criptografada_1 = criptografar(mensagem_1, chave)
    mensagem_criptografada_2 = criptografar(mensagem_2, chave)
    mensagem_criptografada_3 = criptografar(mensagem_3, chave)

    print('*************************************')
    print('Mensagem ---> Mensagem Criptografada')
    print('*************************************')
    print('{} ---> {}'.format(mensagem_1, mensagem_criptografada_1))
    print('{} ---> {}'.format(mensagem_2, mensagem_criptografada_2))
    print('{} ---> {}'.format(mensagem_3, mensagem_criptografada_3))
    print('*************************************')
    

if __name__ == "__main__":
    main()