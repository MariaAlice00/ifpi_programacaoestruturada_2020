def main():
    lista = []


    while True:
        num = int(input())
        if num == 0:
            break
        lista.append(num)

    print(lista)
    contador = contagem(lista)
    print(contador)
    inv = inverso(lista)
    print(inv)
    menor = menor_valor(lista)
    print(menor)
    maior = maior_valor(lista)
    print(maior)
    soma = soma_valores(lista)
    print(soma)


def contagem(lista):
    contador = 0
    for num in lista:
        contador += 1

    return contador


def inverso(lista):
    inv = lista[::-1]

    return inv


def menor_valor(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    
    return menor


def maior_valor(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num

    return maior


def soma_valores(lista):
    soma = 0
    for num in lista:
        soma += num

    return soma
    

if __name__ == "__main__":
    main()    