'''Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de nascimento de uma pessoa, calcule e escreva a idade exata em anos.'''

def idade(ano_atual, ano_nasc):
    return ano_atual - ano_nasc
    
def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())

    if mes_atual == mes_nasc:
        if dia_atual >= dia_nasc:
            print(idade(ano_atual, ano_nasc))
        else:
            print(idade(ano_atual, ano_nasc) - 1)
    elif mes_atual < mes_nasc:
        print(idade(ano_atual, ano_nasc) - 1)
    elif mes_atual > mes_nasc:
        print(idade(ano_atual, ano_nasc))


if __name__ == "__main__":
    main()
