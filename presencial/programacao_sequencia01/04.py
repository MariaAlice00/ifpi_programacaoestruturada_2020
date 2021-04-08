# Ler um valor pelo teclado, converte para inteiro, e guarda na variável 'num_1'
num_1 = int(input('Digite um número: '))
# Ler um valor pelo teclado, converte para inteiro, e guarda na variável 'num_1'
num_2 = int(input('Digite um número: '))
# A variável 'divisao' recebe a divisão inteira de 'num_1' com 'num_2'
divisao = num_1 // num_2
# A variável 'resto' recebe o resto da divisão inteira de 'num_1' com 'num_2'
resto = num_1 % num_2
# Imprime na tela o resto da divisão
print(f'O resto da divisão de {num_1} por {num_2} é {resto}')