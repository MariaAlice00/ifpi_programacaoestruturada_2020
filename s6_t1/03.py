def main():
    maior, menor = maior_menor()
    if maior != 0 and menor != 0:
        print(maior)
        print(menor)


def maior_menor():
    c = 0

    maior = 0
    menor = 0

    while True:
        num = int(input())

        if num == 0: 
            break
        
        if c == 0 and num != 0:
            maior = num
            menor = num
        
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

        c += 1
    
    return maior, menor


if __name__ == "__main__":
    main()