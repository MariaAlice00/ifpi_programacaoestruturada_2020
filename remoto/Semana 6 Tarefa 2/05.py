def main():
    while True:
        nota = float(input())

        if nota <= 10 and nota >= 0:
            if nota_a(nota) == True:
                print('A')
            elif nota_b(nota) == True:
                print('B')
            elif nota_c(nota) == True:
                print('C')
            elif nota_d(nota) == True:
                print('D')
            elif nota_e(nota) == True:
                print('E')
            break
        else:
            print('Nota inválida.')
        

def nota_a(nota):
    return nota >= 8.5


def nota_b(nota):
    return nota >= 7


def nota_c(nota):
    return nota >= 5


def nota_d(nota):
    return nota >= 4


def nota_e(nota):
    return nota >= 0


if __name__ == "__main__":
    main()