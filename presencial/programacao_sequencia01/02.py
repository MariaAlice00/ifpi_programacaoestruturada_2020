# Ler um valor pelo teclado, converte para inteiro, e guarda na variável 'meses'
meses = int(input('Digite uma quantidade de meses: '))
# A variável 'a' recebe a divisão inteira dos meses por 12
a = meses // 12
# A variável 'm' recebe o resto da divisão inteira de meses por 12
m = meses % 12
# Imprime na tela o valor de anos e meses correspondente
print(f'{meses} meses é equivalente a {a} ano(s) {m} meses')