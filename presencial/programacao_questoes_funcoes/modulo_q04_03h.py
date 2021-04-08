#3h. pés em metros

def pes_m(pes):
    return pes / 3.2808

def main():
    pes = float(input('Valor em pés: '))
    pes_m(pes)
    print('{} pés equivalem a {:.2f} metros'.format(pes, pes_m(pes)))

if __name__ == "__main__":
    main()