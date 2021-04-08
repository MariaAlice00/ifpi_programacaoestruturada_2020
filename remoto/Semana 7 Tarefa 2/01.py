def main():
    n = int(input())

    f = fatorial(n)
    print(f)


def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i

    return f


if __name__ == "__main__":
    main()