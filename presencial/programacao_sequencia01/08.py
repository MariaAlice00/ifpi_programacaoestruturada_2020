# A variável 'pi' recebe o valor constante de 3.141592
pi = 3.141592
# Ler um valor pelo teclado, converte para real, e guarda na variável 'raio'
raio = float(input('Digite o raio: '))
# A variável 'area' recebe 'pi' * ('raio' ** 2)
area = pi * (raio ** 2)
# A variável 'area' recebe o resultado da área, arrendodado para duas casas decimais
area = round(area, 2)
# Imprime na tela a área do círculo
print('A área do círculo de raio {} é igual a {}'.format(raio, area))

