def main():
    num = int(input())

    print(eh_primo(num))


def eh_primo(num):
    cont = 0
    for c in range(1, num+1):
        if num % c == 0:
            cont += 1

    if cont == 2:
        return True
    else: 
        return False


if __name__ == "__main__":
    main()