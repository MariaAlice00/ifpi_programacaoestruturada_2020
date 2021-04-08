''' Escreva um programa que gere a seguinte sequência:
            10, 20, 30, 40, ..., 990, 1000.
Considere a separação dos números por vírgula seguido de espaço em branco e o pontos no final da
sequência.'''

def main():
    for c in range(10, 1000, 10):
        print(c, end=', ')
    print('1000.')


if __name__ == "__main__":
    main()