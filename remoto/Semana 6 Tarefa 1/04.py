def main():
    num = int(input())

    novo = inverso(num)
    print(novo)


def separar(num):
    y = 1
    c = 0
    while num / y >= 1:
        x = num // y % 10
        y *= 10
        c += 1
    return c


def inverso(num):
    c = separar(num)
    y = 1
    novo = 0
    
    while num / y >= 1:
        x = num // y % 10
        y *= 10
        n = x * (10 ** (c-1))
        c -= 1
        novo += n

    return novo


if __name__ == "__main__":
    main()