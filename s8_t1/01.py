def main():
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in range(10):
        num[n] = int(input())

    s = soma(num)
    m = multiplicacao(num)

    print(num)
    print(s)
    print(m)


def soma(num):
    soma = 0
    for s in range(10):
        soma += num[s]
    return soma


def multiplicacao(num):
    multiplicacao = 1
    for m in range(10):
        multiplicacao *= num[m]
    return multiplicacao


if __name__ == "__main__":
    main()
