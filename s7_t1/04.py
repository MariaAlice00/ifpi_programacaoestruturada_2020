def main():
    data = int(input())

    num_sorte = numero(data)
    print(num_sorte)


def numero(data):
    soma = 0
    for d in range(8):
        d = data // (10 ** d) % 10
        soma += d

    return soma


if __name__ == "__main__":
    main()