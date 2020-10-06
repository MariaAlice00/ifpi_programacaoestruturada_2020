def main():
    t1 = float(input())
    e1 = input().upper()[0]
    tupla1 = (t1, e1)
    t2 = float(input())
    e2 = input().upper()[0]
    tupla2 = (t2, e2)

    s, e = transformar(t1, t2, e1, e2)
    soma_temperaturas = (s, e)
    print(soma_temperaturas)


def transformar(t1, t2, e1, e2):
    if e1 == 'C':
        if e2 == 'C':
            e = 'C'
        elif e2 == 'F':
            t1 = fahrenheit(t1)
            e = 'F'
    elif e1 == 'F':
        if e2 == 'F':
            e = 'F'
        elif e2 == 'C':
            t1 = celsius(t1)
            e = 'C'

    s = soma(t1, t2)
    
    return s, e


def soma(p, s):
    return round(p + s, 4)


def celsius(t):
    return (t - 32) * (5/9)


def fahrenheit(t):
    return (t * (9/5)) + 32


if __name__ == "__main__":
    main()