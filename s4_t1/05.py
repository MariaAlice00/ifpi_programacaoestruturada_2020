def imc(massa, altura):
    return massa / (altura ** 2)


def classificacao(massa, altura):
    if imc(massa, altura) < 18.5:
        return 'Abaixo do peso'
    elif imc(massa, altura) < 25:
        return 'Peso normal'
    elif imc(massa, altura) < 30:
        return 'Sobrepeso'
    elif imc(massa, altura) < 35:
        return 'Obeso leve'
    elif imc(massa, altura) < 40:
        return 'Obeso moderado'
    elif imc(massa, altura) >= 40:
        return 'Obeso mórbido'


def main():
    massa = float(input())
    altura = float(input())

    print(imc(massa, altura))
    print(classificacao(massa, altura))


if __name__ == "__main__":
    main()