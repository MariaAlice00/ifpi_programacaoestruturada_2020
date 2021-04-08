# Ler um valor pelo teclado, converte para real, e guarda na variável 'nota_a'
nota_a = float(input('Divide a primeira nota: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'nota_b'
nota_b = float(input('Divide a segunda nota: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'nota_c'
nota_c = float(input('Divide a terceira nota: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável 'nota_d'
nota_d = float(input('Divide a quarta nota: '))
# A variável 'somatório' recebe a soma das notas
somatorio = nota_a + nota_b + nota_c + nota_d
# A variável 'media' recebe a divisão da soma das notas por 4
media = somatorio / 4
# A variável 'media' recebe o resultado da média das notas, arrendodado para duas casas decimais
media = round(media, 2)
# Imprime na tela o valor da média
print('A média é: ', media)