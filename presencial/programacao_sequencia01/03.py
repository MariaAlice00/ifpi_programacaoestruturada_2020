# Ler um valor pelo teclado, converte para real, e guarda na variável 'num_1'
num_1 = float(input('Digite um número: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'num_2'
num_2 = float(input('Digite um número: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'num_3'
num_3 = float(input('Digite um número: '))
# A variável 'somatório_1' recebe a soma de 'num_1' e 'num_2'
somatorio_1 = num_1 + num_2
# A variável 'somatório_2' recebe a soma de 'num_2' e 'num_3'
somatorio_2 = num_2 + num_3
# A variável 'multiplicacao' recebe a multiplicação de 'somatorio_1' e 'somatorio_2'
multiplicacao = somatorio_1 * somatorio_2
# Imprime na tela o valor da expressão
print('O resultado da expressão é: ', multiplicacao)