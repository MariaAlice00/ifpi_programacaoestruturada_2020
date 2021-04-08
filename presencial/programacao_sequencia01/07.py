# Ler um valor pelo teclado, converte para real, e guarda na variável 'valor'
valor = float(input('Digite o valor: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'taxa'
taxa = float(input('Digite a porcentagem da taxa: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'tempo'
tempo = float(input('Digite o tempo: '))
# # A variável 'prestacao' recebe 'valor' + ('valor' * ('taxa' / 100) * 'tempo')
prestacao = valor + (valor * (taxa / 100) * tempo)
# A variável 'prestacao' recebe o resultado da prestação, arrendodado para duas casas decimais
prestacao = round(prestacao, 2)
# Imprime na tela o valor da prestação com atraso
print('A prestação com atraso é de R$', prestacao)
