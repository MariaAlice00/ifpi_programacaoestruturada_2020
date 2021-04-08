#3c. °C em K

def celsius_kelvin(c):
    return c + 273.15

def main():
    c = float(input('Valor em °C: '))
    celsius_kelvin(c)
    print('{}°C equivalem a {:.2f}K'.format(c, celsius_kelvin(c)))

if __name__ == '__main__':
    main()