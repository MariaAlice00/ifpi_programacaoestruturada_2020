def main():
    s = soma()
    print(s)


def soma():
    soma = 0

    while True:
        num = int(input())
        
        if num == 0:
            break

        soma += num

    return soma


if __name__ == "__main__":
    main()