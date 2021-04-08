def main():
    n = int(input())

    lista1 = zero(n)
    print(lista1)
    lista2 = sequencia(n)
    print(lista2)
    lista3 = lidos_teclado(n)
    print(lista3)
    lista4 = inverso(n)
    print(lista4)


def zero(n):
    lista_1 = []
    for z in range(n):
        lista_1.append(0)

    return lista_1


def sequencia(n):
    lista2 = []
    for s in range(1, n+1):
        lista2.append(s)
    
    return lista2


def lidos_teclado(n):
    lista3 = []
    for l in range(n):
        num = int(input())
        lista3.append(num)
    
    return lista3


def inverso(n):
    lista4 = []
    for i in range(n):
        num = int(input())
        lista4.append(num)
    
    return lista4[::-1]


if __name__ == "__main__":
    main()