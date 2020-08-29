def certo(resposta):
    return resposta == "variavel"

def main():
    print("No Python, como se chama uma 'caixa' usada para armazenar dados?")
    resposta = input().lower()

    if certo(resposta):
        print(" :) " * 100)
    else:
        print(" :( " * 100)

    print("Obrigada por jogar!")

if __name__ == "__main__":
    main()
