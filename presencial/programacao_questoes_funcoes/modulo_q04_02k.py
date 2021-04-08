#2k. Receber um número inteiro de horas e retornar quantos dias e quantas horas ele corresponde.

def dias_horas(horas):
    return horas // 24, horas % 24

def main():
    horas = int(input('Valor em horas: '))
    d, h = dias_horas(horas)
    print(f'{horas} horas equivalem a {d} dia(s) e {h} hora(s)')

if __name__ == '__main__':
    main()