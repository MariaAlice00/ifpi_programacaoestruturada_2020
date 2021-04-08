'''Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “C” para casado e “S” para solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).'''

def main():
    nome = str(input())
    estado_civil = int(input())

    print(tamanho(nome, estado_civil))

def tamanho(nome, estado_civil):    
    if estado_civil == 1:
        conjugue = str(input())
        quant = len(conjugue) + len(nome)
    else:
        quant = len(nome)

    return quant


if __name__ == "__main__":
    main()