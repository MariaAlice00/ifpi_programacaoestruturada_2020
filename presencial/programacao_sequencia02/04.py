sanduiches = int(input('Quantos sanduíches você quer fazer? '))

queijo_kg = 100 / 1000
presunto_kg = 50 / 1000
hamburguer_kg = 100 / 1000
q = queijo_kg * sanduiches
p = presunto_kg * sanduiches
h = hamburguer_kg * sanduiches

print('Você irá precisar de:')
print('>>> {} kg de queijo'.format(q))
print('>>> {} kg de presunto'.format(p))
print('>>> {} kg de carne'.format(h))
