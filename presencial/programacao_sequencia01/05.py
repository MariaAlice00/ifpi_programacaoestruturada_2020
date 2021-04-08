# Ler um valor pelo teclado, converte para real, e guarda na variável 'salario'
salario = float(input('Digite o salário: '))
# A variável 'desconto' recebe a divisão  de 15 por 100 multiplicado pelo 'salario'
desconto = 15 / 100 * salario
# A variável 'salario_com_desconto' recebe 15 / 100 * 'salario'
salario_com_aumento = desconto + salario
# A variável 'salario_com_desconto' recebe o resultado do salário com aumento, arrendodado para duas casas decimais
salario_com_aumento = round(salario_com_aumento, 2)
# Imprime na tela o salário com aumento de 15%
print('Seu salário com aumento de 15 % é: ', salario_com_aumento)