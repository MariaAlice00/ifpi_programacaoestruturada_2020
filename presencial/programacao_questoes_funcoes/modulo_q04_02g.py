#2g. Receber uma quantidade horas, minutos e segundos e retornar o número inteiro de segundos 
# correspondente.

def main():
    h = int(input('Quantidade de horas: '))
    m = int(input('Quantidade de minutos: '))
    s = int(input('Quantidade de segundos: '))
    segundos(h, m, s)
    print(f'{h} horas {m} minutos e {s} segundos equivalem a {segundos(h, m, s)} segundos')

def segundos(h, m, s):
    return (h * 3600) + (m * 60) + s

if __name__ == '__main__':
    main()