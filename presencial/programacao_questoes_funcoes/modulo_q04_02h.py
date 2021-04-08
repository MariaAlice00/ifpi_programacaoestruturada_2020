#2h. Receber um número inteiro de metros e retornar quantos quilômetros e quantos metros ele 
# corresponde.

def km_m(metro):
    return metro // 1000, metro % 1000

def main():
    metro = int(input('Valor em metros: '))
    km, m = km_m(metro)
    print(f'{metro}m equivalem a {km}km e {m}m')

if __name__ == '__main__':
    main()