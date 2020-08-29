def q1_a(q1):
    return q1 == 'a'

def q1_b(q1):
    return q1 == 'b'

def q1_c(q1):
    return q1 == 'c'

def q2_a(q2):
    return q2 == 'a'

def q2_b(q2):
    return q2 == 'b'

def q2_c(q2):
    return q2 == 'c'

def q3_a(q3):
    return q3 == 'a'

def q3_b(q3):
    return q3 == 'b'

def q3_c(q3):
    return q3 == 'c'
    
    
def main():
    score = 0 

    print('''
    Q1 - Quantos zeros tem o número UM BILHÃO?
    a - seis
    b - sete
    c - dez
    ''')
    q1 = input('>>> ').lower()
    
    if q1_a(q1):
        print('Correto!!!')
        score = score + 1
    elif q1_b(q1):
        print('Quase!')
    elif q1_c(q1):
        print('Um pouco demais, não acha?')
    else:
        print('Você não escolheu a, b ou c')
    print('='*20)


    print('''
    Q2 - Em que ano foi assinada a Lei Áurea no Brasil?
    a - 1788
    b - 1888
    c - 2000
    ''')
    q2 = input('>>> ').lower()

    if q2_a(q2):
        print('Acrescente mais 100 anos e teria a resposta certa!')
    elif q2_b(q2):
        print('Correto!!!')
        score = score + 1
    elif q2_c(q2):
        print('Faz mais tempo que isso!')
    else:
        print('Você não escolheu a, b ou c')
    print('='*20)


    print('''
    Q3 - É uma cidade do Piauí?
    a - Maceió
    b - Gramado
    c - Parnaíba
    ''')
    q3 = input('>>> ').lower()

    if q2_a(q3):
        print('Não! Maceió é a capital de Alagoas.')
    elif q2_b(q3):
        print('Não! Gramado fica no Rio Grande do Sul.')
    elif q2_c(q3):
        print('Correto!!!')
        score = score + 1
    else:
        print('Você não escolheu a, b ou c')
    print('='*20)


    print('Pontuação = {}'.format(score))
    print('Obrigada por jogar!!!')


if __name__ == "__main__":
    main()
