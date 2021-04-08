anos = int(input('Há quantos anos você fuma?: '))
numero = int(input('Quantos cigarros você fuma por dia?: '))
carteira = float(input('Qual o preço de uma carteira de cigarro?: '))

x = (numero * carteira) / 20
y = 365 * anos
z = y * x

print('Você já gastou R$ {:.2f} em cigarros!'. format(z))