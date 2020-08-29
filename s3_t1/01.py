'''Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” 
se for informado o sexo feminino. Use o número inteiro 1 para identificar masculino e 2 para identificar feminino.'''

def masculino(sexo):
    return sexo == 1

def feminino(sexo):
    return sexo == 2

def main():
    nome = str(input())
    sexo = int(input())

    if masculino(sexo):
        print('Ilmo Sr. ' + nome)
    elif feminino(sexo):
        print('Ilma Sra. ' + nome)

if __name__ == "__main__":
    main()
