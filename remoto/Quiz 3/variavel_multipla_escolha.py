def alternativa_a(resposta):
    return resposta == "a"

def alternativa_b(resposta):
    return resposta == "b"

def alternativa_c(resposta):
    return resposta == "c"

def main():
    print('''
    Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
    a - texto
    b - variavel
    c - uma caixa de sapatos
    ''')
    resposta = input().lower()

    if alternativa_a(resposta):
        print(" Não - texto é um tipo de dado :( ")
    elif alternativa_b(resposta):
        print(" Correto!! :) ")
    elif alternativa_c(resposta):
        print(" Não seja bobinho! :( ")
    else:
        print(" Você não escolheu a, b ou c :( ")
        

if __name__ == "__main__":
    main()