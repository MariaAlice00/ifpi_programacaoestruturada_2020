def main():
    n = int(input())
    h = soma(n)
    print(h)


def soma(n):
    den = 1
    h = 0
    while den <= n:
        x = 1 / den
        h += x
        den += 1

    return h


if __name__ == "__main__":
    main()