# Ler um valor pelo teclado, converte para real, e guarda na variável 'dolar'
dolar = float(input('Valor do dólar: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'valor_d'
valor_d = float(input('Valor em dólar: '))
# A variável 'valor_r' recebe a multiplicação de 'valor_d' por 'dolar'
valor_r = valor_d * dolar
# A variável 'valor_r' recebe o resultado de 'valor_r', arrendodado para duas casas decimais
valor_r = round(valor_r, 2)
# Imprime na tela o valor em reais
print('{} dólares é igual a {} reais'.format(valor_d, valor_r))