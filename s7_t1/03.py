def main():
    populacao_a = int(input())
    populacao_b = int(input())

    if populacao_b > populacao_a:
        i = populacao_a
        populacao_a = populacao_b
        populacao_b = i

    t = tempo(populacao_a, populacao_b)
    print(t)

    
def tempo(populacao_a, populacao_b):
    a = populacao_a
    b = populacao_b
    tempo = 0

    while True:
        if b > a:
            break

        aumento_a = 0.02 * a
        aumento_b = 0.03 * b

        a = pop_a(a, aumento_a)
        b = pop_b(b, aumento_b)

        tempo += 1

    return tempo


def pop_a(a, aumento_a):
    return a + aumento_a


def pop_b(b, aumento_b):
    return b + aumento_b


if __name__ == "__main__":
    main()