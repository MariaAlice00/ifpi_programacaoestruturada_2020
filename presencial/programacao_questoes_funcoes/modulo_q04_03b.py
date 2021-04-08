#3b. milhas em quilômetros

def milha_km(milhas):
    return milhas / 0.62137

def main():
    milhas = float(input('Valor em milhas: '))
    milha_km(milhas)
    print(f'{milhas} milhas equivalem a {milha_km(milhas)} km')

if __name__ == '__main__':
    main()

