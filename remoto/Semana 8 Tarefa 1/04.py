def main():
    lista = []
    for c in range(20):
        num = int(input())
        lista.append(num)

    print(lista)

    par, impar = par_impar(lista)

    print(par)
    print(impar)


def par_impar(lista):
    par = []
    impar = []
    for p in lista:
        if p % 2 == 0:
            par.append(p)
        else:
            impar.append(p)

    return par, impar


if __name__ == "__main__":
    main()