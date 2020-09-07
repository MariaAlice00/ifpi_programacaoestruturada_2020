'''Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a média. Considere duas casas decimais.'''

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    print('{:.2f}'.format(media(a, b, c, d, e)))
    maiores(a, b, c, d, e)


def media(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def maiores(a, b, c, d, e):
    if a > media(a, b, c, d, e):
        print(a)
    if b > media(a, b, c, d, e):
        print(b)
    if c > media(a, b, c, d, e):
        print(c)
    if d > media(a, b, c, d, e):
        print(d)
    if e > media(a, b, c, d, e):
        print(e)


if __name__ == "__main__":
    main()