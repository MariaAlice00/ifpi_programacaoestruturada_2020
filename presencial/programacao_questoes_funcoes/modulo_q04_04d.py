#4d. uma função que recebe três valores, por argumento, e retorna verdadeiro se dois dos valores 
# forem iguais. (triângulo isósceles)

def main():
    a = float(input('Primeiro valor: '))
    b = float(input('Segundo valor: '))
    c = float(input('Terceiro valor: '))
    triangulo_isosceles(a, b, c)

def triangulo_isosceles(a, b, c):
    if a == b != c or a == c != b or b == c != a:
        print('Verdadeiro. O triângulo é isósceles.')
    else:
        print('Falso. O triângulo não é isósceles.')

main()
