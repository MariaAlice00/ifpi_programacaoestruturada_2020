#2f. Receber uma quantidade dias, horas e minutos e retornar o número inteiro de minutos 
# correspondente.

def main():
    d = int(input('Quantidade de dias: '))
    h = int(input('Quantidade de horas: '))
    m = int(input('Quantidade de minutos: '))
    minutos(d, h, m)
    print(f'{d} dias {h} horas e {m} minutos equivalem a {minutos(d, h, m)} minutos')

def minutos(d, h, m):
    return (d * 1440) + (h * 60) + m

if __name__ == '__main__':
    main()