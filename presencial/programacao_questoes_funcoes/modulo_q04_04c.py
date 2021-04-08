#4c. uma função que recebe três valores, por argumento, e retorna verdadeiro se os três valores 
# forem diferentes. (triângulo escaleno)

def main():
    a = float(input('Primeiro valor: '))
    b = float(input('Segundo valor: '))
    c = float(input('Terceiro valor: '))
    triangulo_escaleno(a, b, c)

def triangulo_escaleno(a, b, c):
    if a != b != c:
        print('Verdadeiro. O triângulo é escaleno.')
    else:
        print('Falso. O triângulo não é escaleno.')

main()