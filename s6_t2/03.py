def main():
    maior, menor = maior_menor()
    print(maior)
    print(menor)


def maior_menor():
    c = 0

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