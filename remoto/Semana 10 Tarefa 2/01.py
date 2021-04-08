def main():
    texto = input().strip().upper()

    dicionario = letras(texto)
    print(dicionario)


def retirar_acento(texto):
    texto_sem_acento = ''

    for letra in texto:
        if letra == 'Á' or letra == 'À' or letra == 'Ã' or letra == 'Â':
            letra = 'A'
        elif letra == 'É' or letra == 'Ê':
            letra = 'E'
        elif letra == 'Í':
            letra = 'I'
        elif letra == 'Ó' or letra == 'Ô' or letra == 'Õ':
            letra = 'O'
        elif letra == 'Ú':
            letra = 'U'
        else:
            letra = letra

        texto_sem_acento += letra

    return texto_sem_acento


def letras(texto):
    texto_sem_acento = retirar_acento(texto)
    dicionario = dict()

    for c in texto_sem_acento:
        if eh_letra(c):
            if c not in dicionario:
                dicionario[c] = 1
            else:
                dicionario[c] += 1
    
    return dicionario


def eh_letra(c):
    return ord(c) >= 65 and ord(c) <= 90


if __name__ == "__main__":
    main()