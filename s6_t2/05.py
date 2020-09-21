#erro 
def main():
    salario = float(input())
    divida = float(input())

    mes, ano = mes_ano(salario, divida)
    print(f'{mes}/{ano}')


def mes_ano(salario, divida):
    mes = 10
    ano = 2016

    while divida <= salario:
        divida += (15 / 100) * divida
        
        if mes > 12:
            mes = 1
            ano += 1
            
        else:
            if mes == 3:
                aumento = (5 / 100) * salario
                salario += aumento
        mes += 1

    return mes, ano


if __name__ == "__main__":
    main()