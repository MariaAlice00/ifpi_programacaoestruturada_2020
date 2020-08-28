'''Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.'''

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    media = (a + b + c) / 3
    media_especial = media + 1
    if c > 8:
        if media_especial > 10:
            print(10)
        else:
            print(media_especial)
    else:
        print(media)


if __name__ == "__main__":
    main()