#3i. polegadas em centímetros

def pol_cm(pol):
    return pol / 0.39370

def main():
    pol = float(input('Valor em polegadas: '))
    pol_cm(pol)
    print('{} polegadas equivalem a {:.2f} cm'.format(pol, pol_cm(pol)))

if __name__ == "__main__":
    main()