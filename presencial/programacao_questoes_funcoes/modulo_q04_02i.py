#2i. Receber um número inteiro de dias e retornar quantas semanas e quantos dias ele corresponde.

def semanas_dias(dias):
    return dias // 7, dias % 7

def main():
    dias = int(input('Valor em dias: '))
    s, d = semanas_dias(dias)
    print(f'{dias} dias equivalem a {s} semana(s) e {d} dia(s)')

if __name__ == '__main__':
    main()