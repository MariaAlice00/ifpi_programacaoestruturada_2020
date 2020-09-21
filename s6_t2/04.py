'''erro'''

def main():
    num = int(input())

    inverso(num)


def inverso(num):
    y = 1
    while num / y >= 1:
        x = num // y % 10
        y *= 10
        print(x, end='')


if __name__ == "__main__":
    main()