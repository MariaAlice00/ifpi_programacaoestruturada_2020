#3g. metros em pés

def m_pes(metro):
    return metro * 3.2808

def main():
    metro = float(input('Valor em metros: '))
    m_pes(metro)
    print('{} metros equivalem a {:.2f} pés'.format(metro, m_pes(metro)))

if __name__ == "__main__":
    main()