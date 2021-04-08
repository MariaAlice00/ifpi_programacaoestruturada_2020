def q1(a, b, c):
    a == 'a'
    b == 'b'
    c == 'c'
    return a, b, c

def main():
    print('''
    Q1 - Quantos zeros tem o número UM BILHÃO?
    a - seis
    b - sete
    c - dez
    ''')
    q1 = input().lower()
    a, b, c = q1(a, b, c)
    if q1(a):
        print('Correto!!!')
    elif q1(b):
        print('Quase!')
    elif q1(c):
        print('Um pouco demais, não acha?')
    else:
        print('Você não escolheu a, b ou c')

main()