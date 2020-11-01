def montando_placar(nomes):
    nomes = nomes.split()
    nomes = nomes[0] + nomes[2]

    placar = 0
    for letra in nomes:
        if letra in 'aeiou':
            placar += 5
        
        if letra in 'amor':
            placar += 15

    return placar


def main():
    print('Calculadora do Amor\n'+'<3 '*7)

    c = True
    while c == True:
        nomes = input('Digite o nome de 2 pessoas: ').lower()

        placar = montando_placar(nomes)
        print('Seu placar de compatibilidade: {}'.format(placar))

        if placar <= 10:
            print('Esqueça esta pessoa! Nunca vai dar certo!')
        elif placar > 10 and placar < 50:
            print('Pode haver uma chance! Tente!')
        elif placar >= 50 and placar < 80:
            print('Vocês terão um bom relacionamento!')
        elif placar >= 80:
            print('Um relacionamento muito intenso à vista!!! <3')

        continuar = input('Gostaria de continuar?[S/N] ').upper()
        if continuar == 'N':
            c = False
        elif continuar == 'S':
            c = True
        else:
            print('Você digitou algo errado. Tente novamente!')

    print('Obrigada por participar!!!')


if __name__ == "__main__":
    main()
