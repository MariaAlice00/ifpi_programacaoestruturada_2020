def main():
    n = int(input())

    p = 0
    s = 1
    
    print('{}, {}'.format(p, s), end='')

    soma = 0
    cont = 2

    while cont < n:
        soma = p + s
        p = s
        s = soma

        cont += 1

        print(', {}'.format(soma), end='')


if __name__ == "__main__":
    main()
