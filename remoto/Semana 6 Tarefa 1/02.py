def main():
    soma = 0
    c = 0
    while True:
        num = int(input())

        if num == 0:
            break

        soma += num
        c += 1

    m = media(soma, c)
    if m != 0:
        print(m)


def media(soma, c):
    if soma != 0:
        return soma / c
    else:
        return 0


if __name__ == "__main__":
    main()