#3j. centímetros em polegadas

def cm_pol(cm):
    return cm * 0.39370

def main():
    cm = float(input('Valor em centímetros: '))
    cm_pol(cm)
    print('{} cm equivalem a {:.2f} polegadas'.format(cm, cm_pol(cm)))

if __name__ == "__main__":
    main()