#4a. uma função que recebe três valores, por argumento, e retorna verdadeiro se cada um dos valores 
# for menor que a soma dos outros dois. (validação de triângulo)

def main():
    a = float(input('Primeiro valor: '))
    b = float(input('Segundo valor: '))
    c = float(input('Terceiro valor: '))
    validacao_triangulo(a, b, c)

def validacao_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print('Verdadeiro. O triângulo é válido.')
    else:
        print('Falso. O triângulo não é válido.')

main()
