'''Escreva um programa que leia três números por parâmetro e mostre na tela em ordem crescente.'''

def maior(a, b, c):
    if a < b < c:
        print(a)
        print(b)
        print(c)
    elif a < c < b:
        print(a)
        print(c)
        print(b)
    elif b < a < c:
        print(b)
        print(a)
        print(c)
    elif b < c < a:
        print(b)
        print(c)
        print(a)
    elif c < a < b:
        print(c)
        print(a)
        print(b)
    elif c < b < a:
        print(c)
        print(b)
        print(a)


def main():
    a = int(input())
    b = int(input())
    c = int(input())

    maior(a, b, c)


if __name__ == "__main__":
    main()