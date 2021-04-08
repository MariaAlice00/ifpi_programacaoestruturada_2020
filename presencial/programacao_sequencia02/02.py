pequena = int(input('Quantas camisetas pequenas? '))
media = int(input('Quantas camisetas média? '))
grande = int(input('Quantas camisetas grandes? '))

p = pequena * 10
m = media * 12
g = grande * 15
total = p + m + g

print('O valor arrecado será R$ {:.2f}'.format(total))
