#2j. Receber um número inteiro de segundos e retornar quantas horas, quantos minutos e quantos 
# segundos ele corresponde.

def horas_minutos_segundos(segundos):
    h = segundos // 3600
    resto = segundos % 3600
    m = resto // 60
    s = resto % 60
    return h, m, s

def main():
    segundos = int(input('Valor em segundos: '))
    h, m, s = horas_minutos_segundos(segundos)
    print(f'{segundos} segundos equivalem a {h} horas {m} minutos e {s} segundos')

if __name__ == '__main__':
    main()