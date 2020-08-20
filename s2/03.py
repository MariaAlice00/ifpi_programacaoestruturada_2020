def main():
    tempo = int(input())
    horas, minutos, segundos = horario(tempo)
    print('{}:{}:{}'.format(horas, minutos, segundos))

def horario(tempo):
    horas = tempo // 3600
    minutos = (tempo % 3600) // 60
    segundos = (tempo % 3600) % 60
    return horas, minutos, segundos

if __name__ == '__main__':
    main()