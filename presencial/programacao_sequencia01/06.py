# A variável 'pi' recebe o valor constante de 3.141592
pi = 3.141592
# Ler um valor pelo teclado, converte para real, e guarda na variável 'r_m'
r_m = float(input('Digite o valor do raio: '))
# Ler um valor pelo teclado, converte para real, e guarda na variável '_m'
h_m = float(input('Digite o valor da altura: '))
# A variável 'volume' recebe 'pi' * 'r_m' / 2 * h_m
volume = pi * r_m / 2 * h_m
# A variável 'volume' recebe o resultado do volume, arrendodado para duas casas decimais
volume = round(volume, 2)
# Imprime na tela o volume
print(f'O volume da lata de óleo é de {volume}')
