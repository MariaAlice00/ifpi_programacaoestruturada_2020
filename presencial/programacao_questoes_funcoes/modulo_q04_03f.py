#3f. libras em kg

def lb_kg(lb):
    return lb / 2.2046

def main():
    lb = float(input('Valor em libras: '))
    lb_kg(lb)
    print('{}lb equivalem a {:.2f}kg'.format(lb, lb_kg(lb)))

if __name__ == '__main__':
    main()