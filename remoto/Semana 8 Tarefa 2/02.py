def main():
    lista = []


    while True:
        num = int(input())
        if num == 0:
            break
        lista.append(num)

    valor = int(input())

    print(lista)
    print(valor)
    ocorrencias = contador(lista, valor)
    print(ocorrencias)


def contador(lista, valor):
    ocorrencias = 0
    for num in lista:
        if num == valor:
            ocorrencias += 1

    return ocorrencias


if __name__ == "__main__":
    main()