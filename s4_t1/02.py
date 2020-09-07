'''Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.'''

def data1(dia1, mes1, ano1):
    return f'{dia1}/{mes1}/{ano1}'

def data2(dia2, mes2, ano2):
    return f'{dia2}/{mes2}/{ano2}'

def main():
    dia1 = int(input())
    mes1 = int(input())
    ano1 = int(input())

    dia2 = int(input())
    mes2 = int(input())
    ano2 = int(input())

    if ano1 == ano2:
        if mes1 > mes2:
            print(data1(dia1, mes1, ano1))
        elif mes1 == mes2:
            if dia1 > dia2:
                print(data1(dia1, mes1, ano1))
            else:
                print(data2(dia2, mes2, ano2))
        else:
            print(data2(dia2, mes2, ano2))
    elif ano1 > ano2:
        print(data1(dia1, mes1, ano1))
    else:
        print(data2(dia2, mes2, ano2))

if __name__ == "__main__":
    main()