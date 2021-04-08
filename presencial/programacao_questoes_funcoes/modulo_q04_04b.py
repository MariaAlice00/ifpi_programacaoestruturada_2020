#4b. uma função que recebe três valores, por argumento, e retorna verdadeiro se os três valores 
# forem iguais.(triangulo equilátero)

def main():
    a = float(input('Primeiro valor: '))
    b = float(input('Segundo valor: '))
    c = float(input('Terceiro valor: '))
    triangulo_equilatero(a, b, c)

def triangulo_equilatero(a, b, c):
    if a == b == c:
        print('Verdadeiro. O triângulo é equilátero.')
    else:
        print('Falso. O triângulo não é equilátero.')

main()

