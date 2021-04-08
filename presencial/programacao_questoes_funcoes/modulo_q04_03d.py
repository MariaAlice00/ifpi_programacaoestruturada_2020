#3d. K em °C

def kelvin_celsius(k):
    return k - 273.15

def main():
    k = float(input('Valor em K: '))
    kelvin_celsius(k)
    print('{}K equivalem a {:.2f}°C'.format(k, kelvin_celsius(k)))

if __name__ == '__main__':
    main()