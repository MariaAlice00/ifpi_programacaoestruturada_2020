#2m. Receber um número inteiro de minutos e retornar quantos dias, quantas horas e quantos minutos 
# ele corresponde.

def dias_horas_minutos(minutos):
    d = minutos // 1440
    resto = minutos % 1440
    h = resto // 60
    m = resto % 60
    return d, h, m

def main():
    minutos = int(input('Digite o número em minutos: '))
    d, h, m = dias_horas_minutos(minutos)
    print(f'{minutos} minutos equivalem a {d} dia(s) {h} horas(s) e {m} minuto(s)')

if __name__ == '__main__':
    main()