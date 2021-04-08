#2c. Receber uma quantidade de semanas e dias e retornar o número inteiro de dias correspondente.

# 1 semana = 7 dias

def main():
    s = int(input('Quantidade de semanas: '))
    d = int(input('Quantidade de de dias: '))
    dias(s, d)
    print(f'{s} semanas e {d} dias equivalem a {dias(s,d)} dias')

def dias(s, d):
    return 7 * s + d
    
if __name__ == '__main__':
    main()