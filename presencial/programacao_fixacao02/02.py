valor = float(input('Valor da geladeira:'))
desconto = float(input('Percentual do desconto: '))
fator = 1 - desconto / 100
valor = valor * fator
print(f'A geladeira com {desconto}% de desconto fica por {valor:.2f}')
