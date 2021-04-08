'''Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente: Áries (21/03 a 19/04); Touro (20/04 a 20/05); Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07); Leão (23/07 a 22/08); Virgem (23/08 a 22/09); Libra (23/09 a 22/10); Escorpião (23/10 a 21/11); Sagitário (22/11 a 21/12);Capricórnio (22/12 a 19/01); Aquário (20/01 a 18/02); Peixes (19/02 a 20/03);'''

def signos(dia, mes):
    if mes == 3 and 21 <= dia <= 31 or mes == 4 and 1 <= dia <= 19:
        return 'Áries'
    elif mes == 4 and 20 <= dia <= 30 or mes == 5 and 1 <= dia <= 20:
        return 'Touro'
    elif mes == 5 and 21 <= dia <= 31 or mes == 6 and 1 <= dia <= 21:
        return 'Gêmeos'
    elif mes == 6 and 22 <= dia <= 30 or mes == 7 and 1 <= dia <= 22:
        return 'Câncer'
    elif mes == 7 and 23 <= dia <= 31 or mes == 8 and 1 <= dia <= 22:
        return 'Leão'
    elif mes == 8 and 23 <= dia <= 31 or mes == 9 and 1 <= dia <= 22:
        return 'Virgem'
    elif mes == 9 and 23 <= dia <= 30 or mes == 10 and 1 <= dia <= 22:
        return 'Libra'
    elif mes == 10 and 23 <= dia <= 31 or mes == 11 and 1 <= dia <= 21:
        return 'Escorpião'
    elif mes == 11 and 22 <= dia <= 30 or mes == 12 and 1 <= dia <= 21:
        return 'Sagitário'
    elif mes == 12 and 22 <= dia <= 31 or mes == 1 and 1 <= dia <= 19:
        return 'Capricórnio'
    elif mes == 1 and 20 <= dia <= 31 or mes == 2 and 1 <= dia <= 18:
        return 'Aquário'
    elif mes == 2 and 19 <= dia <= 28 or mes == 3 and 1 <= dia <= 20:
        return 'Peixes'


def main():
    dia = int(input())
    mes = int(input())

    print(signos(dia, mes))


if __name__ == "__main__":
    main()