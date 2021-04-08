#2d. Receber uma quantidade de semanas, dias e horas e retornar o número inteiro de horas 
# correspondente.

def main():
    s = int(input('Quantidade de semanas: '))
    d = int(input('Quantidade de de dias: '))
    h = int(input('Quantidade de horas: '))
    horas(s, d, h)
    print(f'{s} semanas {d} dias e {h} horas equivalem a {horas(s, d, h)} horas')

def horas(s, d, h):
    return (s * 168) + (d * 24) + h

if __name__ == '__main__':
    main()