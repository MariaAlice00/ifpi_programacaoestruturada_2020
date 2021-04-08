def main():
    t1 = float(input())
    e1 = input().upper()[0]
    tupla1 = (t1, e1)
    t2 = float(input())
    e2 = input().upper()[0]
    tupla2 = (t2, e2)

    x, y = transformar(t1, t2, e1, e2)

    if x > y:
        maior = tupla1
    elif y > x:
        maior = tupla2

    print(maior)


def transformar(t1, t2, e1, e2):
    if e1 == 'C':
        x = t1
        if e2 == 'F':
            y = celsius(t2)
        elif e2 == 'C':
            y = t2
    elif e1 == 'F':
        x = celsius(t1)
        if e2 == 'F':
            y = celsius(t2)
        elif e2 == 'C':
            y = t2

    return x, y


def celsius(t):
    return (t - 32) * (5/9)


if __name__ == "__main__":
    main()