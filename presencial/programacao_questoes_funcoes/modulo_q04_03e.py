#3e. kg em libras

def kg_lb(kg):
    return kg * 2.2046

def main():
    kg = float(input('Valor em quilogramas(kg): '))
    kg_lb(kg)
    print('{}kg equivalem a {:.2f} lb'.format(kg, kg_lb(kg)))

if __name__ == '__main__':
    main()