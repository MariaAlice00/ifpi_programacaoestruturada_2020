def main():
    num_pessoas = 0
    soma = 0

    while True:
        idade = int(input())
    
        if idade == 0:
            break

        num_pessoas += 1
        soma += idade

        if num_pessoas == 1 and idade != 0:
            maior = idade
            menor = idade

        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade

    if num_pessoas != 0:
        idade_media = soma / num_pessoas

        print(num_pessoas)
        print('{:.2f}'.format(idade_media))
        print(menor)
        print(maior)


if __name__ == "__main__":
    main()