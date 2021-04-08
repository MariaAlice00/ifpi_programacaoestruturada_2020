x_1 = int(input('Digite a abscissa do ponto 1: '))
x_2 = int(input('Digite a abscissa do ponto 2: '))
y_1 = int(input('Digite a ordenada do ponto 1: '))
y_2 = int(input('Digite a ordenada do ponto 2: '))

d = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
D = d ** (1/2)

print('A distância entre os pontos é igual a {:.2f}'.format(D))
