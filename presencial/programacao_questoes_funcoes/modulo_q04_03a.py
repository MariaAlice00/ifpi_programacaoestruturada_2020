#3a. quilômetro em milhas

def km_milha(quilometro):
    return quilometro * 0.62137

def main():
    quilometro = float(input('Valor em quilômetros: '))
    km_milha(quilometro)
    print(f'{quilometro} km equivalem a {km_milha(quilometro)} milhas')

if __name__ == '__main__':
    main()

