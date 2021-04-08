def main():
    vantagem = float(input())

    minutos = tempo(vantagem)
    print(minutos)
    

def tempo(vantagem):
    tartaruga = vantagem
    lebre = 0
    minutos = 0

    if vantagem == 0:
        minutos = 0
    else:
        while lebre < tartaruga:
            lebre += 10
            tartaruga += 1
            minutos += 1
        
    return minutos


if __name__ == "__main__":
    main()