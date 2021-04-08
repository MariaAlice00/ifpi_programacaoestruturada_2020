# Ler um valor pelo teclado, converte para inteiro, e guarda na variável 'c'
c = int(input('Digite a temperatura em °C: '))
# A variável 'f' recebe (9 * 'c' + 160) / 5
f = (9 * c + 160) / 5
# Imprime na tela o valor da temperatura em graus Fahrenheit
print('{} °C é equivalente a {} °F'.format(c, f))
